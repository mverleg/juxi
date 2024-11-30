from datetime import datetime, timedelta
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


def _next_occurrence_month(now: datetime, next: datetime, every_nth: int):
    print('')

    month_diff_pure = (now.year * 12 + now.month) - (next.year * 12 + next.month)
    if (now.day, now.hour, now.minute) < (next.day, next.hour, next.minute):
        # if they were the same month, `next` would be before `now`, so aim one month later
        month_diff_pure += 1

    if month_diff_pure < 0:
        # need to shift backwards; round down to still be in the future
        month_diff_round = floor(month_diff_pure / every_nth) * every_nth
    else:
        # need to shift forwards, round up to be in the future
        month_diff_round = ceil(month_diff_pure / every_nth) * every_nth

    print(f'first event from {next.date()} after {now.date()} in steps of {every_nth} months: {month_diff_round}')

    # month_diff_steps = (month_diff_pure // every_nth) * every_nth
    # next = _add_months(next, month_diff_steps)
    # print('month_diff_pure', month_diff_steps, month_diff_steps)
    # print('next', next)
    # while next > now:
    #     print(f'next = _add_months({next}, -{every_nth})')
    #     next = _add_months(next, -every_nth)
    #     print('subtract another', every_nth, 'next', next)
    # else:
    #     print('no extra - shift')
    # while next < now:
    #     next = _add_months(next, every_nth)
    #     print('add another', every_nth, 'next', next)
    # else:
    #     print('no extra + shift')
    # # next.replace(year=now.year, month=now.month)
    # # if next < now:
    # #     next.replace(month=now.month + 1)
    # #TODO @mark: this only works if every_nth is 1

    assert next > now
    return next


def _add_months(dt: datetime, add_months: int) -> datetime:
    if add_months > 0:
        return dt + relativedelta(month=add_months)
    else:
        #TODO @mark: is this `if` needed?
        return dt - relativedelta(month=-add_months)

