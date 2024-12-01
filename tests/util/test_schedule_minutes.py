
from datetime import datetime

import pytz

from juxi.data.schedule import HOUR, MINUTE
from juxi.util.schedule import next_occurrence

TZ = pytz.timezone("Europe/Amsterdam")


def test_forward_sameday():
    event = next_occurrence(now=tim(10, 14, 30), reference=tim(1, 10, 20), time_unit=MINUTE, every_nth=15)
    assert event == tim(10, 14, 35)

def test_forward_nextday():
    event = next_occurrence(now=tim(10, 23, 55), reference=tim(1, 1, 20), time_unit=MINUTE, every_nth=75)
    assert event == tim(11, 0, 5)

def test_backwards_sameday():
    event = next_occurrence(now=tim(10, 12, 30), reference=tim(1, 14, 20), time_unit=MINUTE, every_nth=15)
    assert event == tim(10, 12, 35)

def test_backwards_nextday():
    event = next_occurrence(now=tim(10, 20, 00), reference=tim(30, 19, 20), time_unit=MINUTE, every_nth=6*60)
    assert event == tim(11, 1, 20)

def test_hour_same_as_60mins():
    event = next_occurrence(now=tim(10, 12, 30), reference=tim(1, 16, 0), time_unit=HOUR, every_nth=2)
    assert event == tim(10, 14, 0)

def test_strip_seconds():
    event = next_occurrence(now=datetime(2024, 11, 1, 1, 40, 20, 30, tzinfo=TZ),
        reference=datetime(2024, 2, 1, 2, 10, 40, 50, tzinfo=TZ), time_unit=MINUTE, every_nth=30)
    assert event.minute == 40
    assert event.second == 0
    assert event.microsecond == 0

def test_very_long():
    event = next_occurrence(now=datetime(1971, 1, 1, 0, 4, tzinfo=TZ), reference=datetime(9999, 12, 31, 23, 59, tzinfo=TZ), time_unit=MINUTE, every_nth=3)
    assert event == datetime(1971, 1, 1, 0, 5, tzinfo=TZ)

def tim(day, hour, minute):
    return datetime(2024, 11, day, hour, minute, 0, 0, tzinfo=TZ)

def test_reproduce_broken_case_1():
    event = next_occurrence(now=tim(10, 12, 30), reference=tim(1, 16, 0), time_unit=MINUTE, every_nth=120)
    assert event == tim(10, 14, 0)

