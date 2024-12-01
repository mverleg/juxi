
from datetime import datetime

import pytz

from juxi.data.schedule import WEEK, DAY
from juxi.util.schedule import next_occurrence

TZ = pytz.timezone("Europe/Amsterdam")


def test_forward_samemonth():
    event = next_occurrence(now=dt(2024, 9, 25, 1), reference=dt(2024, 6, 1, 2), time_unit=DAY, every_nth=29)
    assert event == dt(2024, 9, 25, 2)

def test_forward_nextmonth():
    event = next_occurrence(now=dt(2024, 9, 21, 2), reference=dt(2024, 6, 1, 1), time_unit=DAY, every_nth=28)
    assert event == dt(2024, 10, 19, 1)

def test_forward_nextmonth_shorter():
    event = next_occurrence(now=dt(2024, 9, 30, 12), reference=dt(2024, 8, 26, 11), time_unit=DAY, every_nth=6)
    assert event == dt(2024, 10, 1, 11)

def test_backard_samemonth():
    event = next_occurrence(now=dt(2024, 4, 10, 2), reference=dt(2024, 4, 30, 1), time_unit=DAY, every_nth=5)
    assert event == dt(2024, 4, 15, 1)

def test_backard_nextmonth():
    event = next_occurrence(now=dt(2024, 3, 31, 1), reference=dt(2024, 4, 14, 2), time_unit=DAY, every_nth=7)
    assert event == dt(2024, 3, 31, 2)

def test_backard_nextmonth_shorter():
    event = next_occurrence(now=dt(2024, 3, 31, 3), reference=dt(2024, 4, 14, 2), time_unit=DAY, every_nth=7)
    assert event == dt(2024, 4, 7, 2)

def test_forward_cross_year():
    event = next_occurrence(now=dt(2024, 12, 25, 2), reference=dt(2024, 12, 1, 1), time_unit=DAY, every_nth=8)
    assert event == dt(2025, 1, 2, 1)

def test_backwards_cross_year():
    event = next_occurrence(now=dt(2024, 12, 25, 2), reference=dt(2025, 1, 12, 1), time_unit=DAY, every_nth=8)
    assert event == dt(2024, 12, 27, 1)

def test_feb_nonleap_year():
    event = next_occurrence(now=dt(2023, 2, 26, 23), reference=dt(2023, 2, 2, 1), time_unit=DAY, every_nth=2)
    assert event == dt(2023, 2, 28, 1)

def test_feb_leap_year():
    event = next_occurrence(now=dt(2024, 2, 27, 23), reference=dt(2024, 2, 3, 1), time_unit=DAY, every_nth=2)
    assert event == dt(2024, 2, 29, 1)

def test_weeks_same_as_7days():
    event = next_occurrence(now=dt(2024, 8, 28, 1), reference=dt(2024, 7, 31, 2), time_unit=WEEK, every_nth=1)
    assert event == dt(2024, 8, 28, 2)

def test_strip_seconds():
    event = next_occurrence(now=datetime(2024, 11, 1, 1, 55, 20, 30, tzinfo=TZ),
        reference=datetime(2024, 2, 1, 2, 10, 40, 50, tzinfo=TZ), time_unit=DAY, every_nth=3)
    assert event.minute == 10
    assert event.second == 0
    assert event.microsecond == 0

def test_very_long():
    event = next_occurrence(now=dt(1971, 1, 15, 2), reference=dt(9999, 12, 31, 4), time_unit=DAY, every_nth=1)
    assert event == dt(1971, 1, 15, 4)

def test_reproduce_broken_case_1():
    event = next_occurrence(now=dt(2024, 3, 31, 1), reference=dt(2024, 4, 12, 2), time_unit=DAY, every_nth=6)
    assert event == dt(2024, 3, 31, 2)


def dt(year, month, day, hour):
    return datetime(year, month, day, hour, 15, 0, 0, tzinfo=TZ)

