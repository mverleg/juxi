from datetime import datetime, timedelta
from urllib.parse import urlparse, urlunparse

from django.http import QueryDict
from django.urls import reverse

from juxi.models import Schedule, MONTH, WEEK, DAY, HOUR, MINUTE


def next_occurrence(date_reference: datetime, time_unit: str, every_nth: int, now: datetime) -> datetime:
    assert every_nth > 0

    if time_unit == MONTH:
        next.replace(year=now.year, month=now.month)
        if next < now:
            next.replace(month=now.month + 1)
        #TODO @mark: this only works if every_nth is 1
        return next
    if time_unit in {WEEK, DAY}:
        return now  #TODO @mark:
    if time_unit in {HOUR, MINUTE}:
        return now  #TODO @mark:
    raise AssertionError(f"unknown time unit {time_unit}")

