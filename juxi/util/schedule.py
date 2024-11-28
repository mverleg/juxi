from datetime import datetime, timedelta

from django.utils import timezone

from juxi.data.schedule import MONTH, WEEK, DAY, HOUR, MINUTE


def next_occurrence(now: datetime, reference: datetime, time_unit: str, every_nth: int) -> datetime:
    assert every_nth > 0
    assert timezone.is_aware(reference)
    assert timezone.is_aware(now)
    print(now)

    next = reference.replace(second=0, microsecond=0)
    if time_unit == MONTH:
        month_diff = (reference.year * 12 + reference.month) - (now.year * 12 + now.month)
        next.replace(year=next.year + month_diff // 12, month=next.month + month_diff % 12)
        # next.replace(year=now.year, month=now.month)
        # if next < now:
        #     next.replace(month=now.month + 1)
        #TODO @mark: this only works if every_nth is 1
        return next
    if time_unit in {WEEK, DAY}:
        return now  #TODO @mark:
    if time_unit in {HOUR, MINUTE}:
        return now  #TODO @mark:
    raise AssertionError(f"unknown time unit {time_unit}")

