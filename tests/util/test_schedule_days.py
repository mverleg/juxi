
from datetime import datetime

from juxi.data.schedule import WEEK, DAY
from juxi.util.schedule import next_occurrence
from tests.util.test_schedule_util import dt, TZ


def test_interyear_forward_samemonth():
    event = next_occurrence(now=dt(2024, 11, 1, 1), reference=dt(2023, 2, 1, 2), time_unit=DAY, every_nth=3)
    assert event == dt(2024, 11, 1, 2)

def test_interyear_forward_samemonth_shorter():
    event = next_occurrence(now=dt(2024, 11, 1, 1), reference=dt(2023, 5, 31, 23), time_unit=DAY, every_nth=3)
    assert event == dt(2024, 11, 30, 23)

def test_interyear_forward_nextmonth():
    event = next_occurrence(now=dt(2024, 10, 1, 2), reference=dt(2023, 2, 1, 1), time_unit=DAY, every_nth=3)
    assert event == dt(2024, 11, 1, 1)

def test_interyear_forward_nextmonth_shorter():
    event = next_occurrence(now=dt(2024, 4, 30, 1), reference=dt(2023, 1, 31, 2), time_unit=DAY, every_nth=3)
    assert event == dt(2024, 4, 30, 2)

def test_interyear_backard_samemonth():
    event = next_occurrence(now=dt(2024, 4, 1, 1), reference=dt(2026, 7, 1, 2), time_unit=DAY, every_nth=3)
    assert event == dt(2024, 4, 1, 2)

def test_interyear_backard_samemonth_shorter():
    event = next_occurrence(now=dt(2024, 4, 1, 1), reference=dt(2026, 10, 31, 23), time_unit=DAY, every_nth=3)
    assert event == dt(2024, 4, 30, 23)

def test_interyear_backard_nextmonth():
    event = next_occurrence(now=dt(2024, 4, 1, 2), reference=dt(2026, 7, 1, 1), time_unit=DAY, every_nth=3)
    assert event == dt(2024, 7, 1, 1)

def test_interyear_backard_nextmonth_shorter():
    event = next_occurrence(now=dt(2024, 11, 15, 23), reference=dt(2026, 8, 31, 22), time_unit=DAY, every_nth=3)
    assert event == dt(2024, 11, 30, 22)

def test_feb_nonleap_year():
    event = next_occurrence(now=dt(2023, 2, 28, 1), reference=dt(2023, 1, 31, 2), time_unit=DAY, every_nth=1)
    assert event == dt(2023, 2, 28, 2)

def test_feb_leap_year():
    event = next_occurrence(now=dt(2024, 2, 28, 1), reference=dt(2024, 1, 31, 2), time_unit=DAY, every_nth=1)
    assert event == dt(2024, 2, 29, 2)

def test_weeks_same_as_7days():
    #TODO @mark: more cases?
    event = next_occurrence(now=dt(2024, 2, 28, 1), reference=dt(2024, 1, 31, 2), time_unit=WEEK, every_nth=1)
    assert event == dt(2024, 2, 29, 2)

def test_strip_seconds():
    event = next_occurrence(now=datetime(2024, 11, 1, 1, 55, 20, 30, tzinfo=TZ),
        reference=datetime(2024, 2, 1, 2, 10, 40, 50, tzinfo=TZ), time_unit=DAY, every_nth=3)
    assert event.minute == 10
    assert event.second == 0
    assert event.microsecond == 0
