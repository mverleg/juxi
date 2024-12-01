from calendar import monthrange
from datetime import datetime

from dateutil.relativedelta import relativedelta
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
        print(f'TODO: {time_unit}')
        return now  #TODO @mark:
    if time_unit in {HOUR, MINUTE}:
        print(f'TODO: {time_unit}')
        return now  #TODO @mark:
    raise AssertionError(f"unknown time unit {time_unit}")


def _next_occurrence_month(now: datetime, reference: datetime, every_nth: int):
    print('')

    #TODO @mark: to handle shorter months, just shift 1 day of month, then add back and ceil at end

    month_diff_round = _find_month_shift(every_nth, now, reference)

    next = _perform_month_shift(month_diff_round, reference)

    if next <= now:
        # this can (only?) happen when reference and now are on e.g. 31,
        # but now is later than reference, so it rolls over to next month with 30 days
        next = _perform_month_shift(month_diff_round + every_nth, reference)

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
        month_diff_round = round_away_from_zero(month_diff_pure, every_nth) * every_nth
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


def round_away_from_zero(num, div) -> int:
    return int(float(num + div - 1) / div)


def _add_months(dt: datetime, add_months: int) -> datetime:
    if add_months > 0:
        return dt + relativedelta(month=add_months)
    else:
        #TODO @mark: is this `if` needed?
        return dt - relativedelta(month=-add_months)

