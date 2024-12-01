from calendar import monthrange
from datetime import datetime, timedelta

from django.utils import timezone

from juxi.data.schedule import MONTH, WEEK, DAY, HOUR, MINUTE


#TODO: not sure if/now this handles DST or timezone redefinitions, but I'm willing to accept being slightly off in those cases

def next_occurrence(now: datetime, reference: datetime, time_unit: str, every_nth: int) -> datetime:
    assert every_nth > 0
    assert timezone.is_aware(reference)
    assert timezone.is_aware(now)
    print(now)

    next = reference.replace(second=0, microsecond=0)
    if time_unit == MONTH:
        return _next_occurrence_month(now, next, every_nth)
    if time_unit in {WEEK, DAY}:
        step_days_pure = every_nth * 7 if time_unit == WEEK else every_nth
        return _next_occurrence_days(now, reference, step_days_pure)
    if time_unit in {HOUR, MINUTE}:
        step_minutes_pure = every_nth * 60 if time_unit == HOUR else every_nth
        return _next_occurrence_minutes(now, reference, step_minutes_pure)
    raise AssertionError(f"unknown time unit {time_unit}")


def _next_occurrence_days(now, reference, every_nth_day):
    diff = now - reference
    step_days_pure = diff.days
    if (reference.hour, reference.minute) < (now.hour, now.minute):
        # if they were the same day, `next` would be before `now`, so aim one day later
        step_days_pure += 1
    if diff.days < 0:
        # need to shift backwards; round down to still be in the future
        step_days_round = _div_round_towards_zero(step_days_pure, every_nth_day) * every_nth_day
    else:
        # need to shift forwards, round up to be in the future
        step_days_round = _round_away_from_zero(step_days_pure, every_nth_day) * every_nth_day
    next = reference + timedelta(days=step_days_round)
    if next <= now:
        next = reference + timedelta(days=step_days_round + every_nth_day)
    assert next > now
    return next.replace(second=0, microsecond=0)


def _next_occurrence_minutes(now, reference, every_nth_min):
    # This always considers the time within the day, so if the shift is e.g. 7 hours from 12:00,
    # it will reset to the reference time tomorrow, so 5:00, 12:00, ... not wrapped like 2:00, 9:00

    now_total_mins = now.hour * 60 + now.minute
    ref_total_mins = reference.hour * 60 + reference.minute
    minute_round_total = _find_rounded_minute_total(every_nth_min, now_total_mins, ref_total_mins)

    if minute_round_total >= 24 * 60:
        # next day; find first occurrence
        next = now + timedelta(days=1)
        minute_round_total = _find_rounded_minute_total(every_nth_min, 0, ref_total_mins)
        assert minute_round_total < 24 * 60
    else:
        next = now

    return next.replace(
        hour=minute_round_total // 60,
        minute=minute_round_total % 60,
        second=0,
        microsecond=0)


def _find_rounded_minute_total(every_nth_min, now_total_mins, ref_total_mins):
    minute_diff_pure = now_total_mins - ref_total_mins
    if now_total_mins < ref_total_mins:
        # need to shift backwards; round down to still be in the future
        minute_diff_round = _div_round_towards_zero(minute_diff_pure, every_nth_min) * every_nth_min
    else:
        # need to shift forwards, round up to be in the future
        minute_diff_round = _round_away_from_zero(minute_diff_pure, every_nth_min) * every_nth_min
    return ref_total_mins + minute_diff_round


def _next_occurrence_month(now: datetime, reference: datetime, every_nth_month: int):

    month_diff_round = _find_month_shift(every_nth_month, now, reference)

    next = _perform_month_shift(month_diff_round, reference)

    if next <= now:
        # this can (only?) happen when reference and now are on e.g. 31,
        # but now is later than reference, so it rolls over to next month with 30 days
        next = _perform_month_shift(month_diff_round + every_nth_month, reference)

    # assert next > now
    # assert reference.day == next.day or reference.day > 28
    return next


def _find_month_shift(every_nth, now, reference):
    month_diff_pure = (now.year * 12 + now.month) - (reference.year * 12 + reference.month)
    if (reference.day, reference.hour, reference.minute) < (now.day, now.hour, now.minute):
        # if they were the same month, `next` would be before `now`, so aim one month later
        month_diff_pure += 1
    if month_diff_pure < 0:
        # need to shift backwards; round down to still be in the future
        month_diff_round = _div_round_towards_zero(month_diff_pure, every_nth) * every_nth
    else:
        # need to shift forwards, round up to be in the future
        month_diff_round = _round_away_from_zero(month_diff_pure, every_nth) * every_nth
    return month_diff_round


def _perform_month_shift(month_diff_round, reference):
    delta_months = reference.month + month_diff_round - 1
    next_year = reference.year + delta_months // 12
    next_month = delta_months % 12 + 1
    return reference.replace(
        year=next_year,
        month=next_month,
        day=min(monthrange(next_year, next_month)[1], reference.day),
    )


def _div_round_towards_zero(num, div) -> int:
    return int(float(num) / div)


def _round_away_from_zero(num, div) -> int:
    return int(float(num + div - 1) / div)


def _add_months(dt: datetime, add_months: int) -> datetime:
    if add_months > 0:
        return dt + relativedelta(month=add_months)
    else:
        #TODO @mark: is this `if` needed?
        return dt - relativedelta(month=-add_months)

