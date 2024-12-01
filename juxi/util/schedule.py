from calendar import monthrange
from datetime import datetime
from math import floor, ceil

from dateutil.relativedelta import relativedelta
from django.utils import timezone

from juxi.data.schedule import MONTH, WEEK, DAY, HOUR, MINUTE


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

    print(f'first event from {reference.date()} after {now.date()} in steps of {every_nth} months: {month_diff_round}')

    next = _perform_month_shift(month_diff_round, reference)

    print(f'{now.year}, {now.month} -> +{month_diff_round // 12}yr, {(now.month + month_diff_round - 1) % 12 + 1 - now.month}m -> {next.year}, {next.month}')

    print(f'next > now -> {next} > {now}')
    assert next > now
    return next


def _find_month_shift(every_nth, now, reference):
    month_diff_pure = (now.year * 12 + now.month) - (reference.year * 12 + reference.month)
    if (reference.day, reference.hour, reference.minute) < (now.day, now.hour, now.minute):
        # if they were the same month, `next` would be before `now`, so aim one month later
        print(f'  +1 month_diff_pure={month_diff_pure}+1 between now {now} and reference {reference}')
        month_diff_pure += 1
    else:
        print(f'  just month_diff_pure={month_diff_pure} between now {now} and reference {reference}')
    if month_diff_pure < 0:
        # need to shift backwards; round down to still be in the future
        print('need to shift backwards; round down to still be in the future')
        month_diff_round = floor(month_diff_pure / every_nth) * every_nth
    else:
        # need to shift forwards, round up to be in the future
        print('need to shift forwards, round up to be in the future')
        month_diff_round = ceil(month_diff_pure / every_nth) * every_nth
    return month_diff_round


def _perform_month_shift(month_diff_round, reference):
    delta_months = reference.month + month_diff_round - 1
    next_year = reference.year + delta_months // 12
    next_month = delta_months % 12 + 1
    print(f'  {reference.year} + ({reference.month} + {month_diff_round} - 1) // 12 = {reference.year} + {delta_months} // 12 = {next_year}')
    return reference.replace(
        year=next_year,
        month=next_month,
        day=min(monthrange(next_year, next_month)[1], reference.day),
    )


def _add_months(dt: datetime, add_months: int) -> datetime:
    if add_months > 0:
        return dt + relativedelta(month=add_months)
    else:
        #TODO @mark: is this `if` needed?
        return dt - relativedelta(month=-add_months)

