
from datetime import datetime
import pytz

from juxi.data.schedule import MONTH
from juxi.util.schedule import next_occurrence

TZ = pytz.timezone("Europe/Amsterdam")

def test_interyear_forward_samemonth():
    event = next_occurrence(now=dt(2024, 11, 1, 1), reference=dt(2023, 2, 1, 2), time_unit=MONTH, every_nth=3)
    assert event == dt(2024, 11, 1, 2)

def test_interyear_forward_samemonth_shorter():
    event = next_occurrence(now=dt(2024, 11, 1, 1), reference=dt(2023, 5, 31, 23), time_unit=MONTH, every_nth=3)
    assert event == dt(2024, 11, 30, 23)

def test_intrayear_forward_samemonth():
    event = next_occurrence(now=dt(2024, 11, 1, 1), reference=dt(2024, 3, 1, 23), time_unit=MONTH, every_nth=4)
    assert event == dt(2024, 11, 1, 23)

def test_intrayear_forward_samemonth_shorter():
    event = next_occurrence(now=dt(2024, 11, 15, 1), reference=dt(2024, 7, 31, 2), time_unit=MONTH, every_nth=4)
    assert event == dt(2024, 11, 30, 2)

def test_interyear_forward_nextmonth():
    event = next_occurrence(now=dt(2024, 10, 1, 2), reference=dt(2023, 2, 1, 1), time_unit=MONTH, every_nth=3)
    assert event == dt(2024, 11, 1, 1)

def test_interyear_forward_nextmonth_shorter():
    event = next_occurrence(now=dt(2024, 4, 30, 1), reference=dt(2023, 1, 31, 2), time_unit=MONTH, every_nth=3)
    assert event == dt(2024, 4, 30, 2)

def test_intrayear_forward_nextmonth():
    event = next_occurrence(now=dt(2024, 11, 1, 1), reference=dt(2024, 3, 1, 23), time_unit=MONTH, every_nth=4)
    assert event == dt(2024, 11, 1, 23)

def test_intrayear_forward_nextmonth_shorter():
    event = next_occurrence(now=dt(2024, 11, 15, 1), reference=dt(2024, 7, 31, 2), time_unit=MONTH, every_nth=4)
    assert event == dt(2024, 11, 30, 2)

def test_interyear_backard_samemonth():
    event = next_occurrence(now=dt(2024, 4, 1, 1), reference=dt(2026, 7, 1, 2), time_unit=MONTH, every_nth=3)
    assert event == dt(2024, 4, 1, 2)

def test_interyear_backard_samemonth_shorter():
    event = next_occurrence(now=dt(2024, 4, 1, 1), reference=dt(2026, 10, 31, 23), time_unit=MONTH, every_nth=3)
    assert event == dt(2024, 4, 30, 23)

def test_intrayear_backard_samemonth():
    event = next_occurrence(now=dt(2024, 4, 1, 1), reference=dt(2024, 12, 11, 23), time_unit=MONTH, every_nth=4)
    assert event == dt(2024, 4, 11, 23)

def test_intrayear_backard_samemonth_shorter():
    event = next_occurrence(now=dt(2024, 4, 15, 1), reference=dt(2024, 8, 31, 2), time_unit=MONTH, every_nth=4)
    assert event == dt(2024, 4, 30, 2)

def test_interyear_backard_nextmonth():
    event = next_occurrence(now=dt(2024, 4, 1, 2), reference=dt(2026, 7, 1, 1), time_unit=MONTH, every_nth=3)
    assert event == dt(2024, 7, 1, 1)
    assert False  #TODO @mark:

def test_interyear_backard_nextmonth_shorter():
    event = next_occurrence(now=dt(2024, 4, 31, 1), reference=dt(2026, 10, 1, 23), time_unit=MONTH, every_nth=3)
    assert event == dt(2026, 10, 1, 23)
    assert False  #TODO @mark:

def test_intrayear_backard_nextmonth():
    event = next_occurrence(now=dt(2024, 4, 1, 1), reference=dt(2024, 12, 11, 23), time_unit=MONTH, every_nth=4)
    assert event == dt(2024, 4, 11, 23)
    assert False  #TODO @mark:

def test_intrayear_backard_nextmonth_shorter():
    event = next_occurrence(now=dt(2024, 4, 15, 1), reference=dt(2024, 8, 31, 2), time_unit=MONTH, every_nth=4)
    assert event == dt(2024, 4, 30, 2)
    assert False  #TODO @mark:

def test_rounding_towards_zero_instead_of_floor():
    event = next_occurrence(now=dt(2024, 6, 1, 2), reference=dt(2026, 7, 1, 1), time_unit=MONTH, every_nth=5)
    assert event == dt(2024, 11, 1, 1)

def test_interyear_backwards_step_not_divisor_of_12():
    event = next_occurrence(now=dt(2024, 6, 1, 1), reference=dt(2026, 7, 1, 2), time_unit=MONTH, every_nth=5)
    assert event == dt(2024, 6, 1, 2)

def test_interyear_forward_step_not_divisor_of_12():
    event = next_occurrence(now=dt(2024, 6, 1, 2), reference=dt(2022, 5, 1, 1), time_unit=MONTH, every_nth=5)
    assert event == dt(2024, 11, 1, 1)

def test_nochange_sameday():
    event = next_occurrence(now=dt(2024, 7, 15, 2), reference=dt(2024, 7, 15, 3), time_unit=MONTH, every_nth=3)
    assert event == dt(2024, 7, 15, 3)

def test_nochange_endofmonth():
    event = next_occurrence(now=dt(2024, 7, 1, 23), reference=dt(2024, 7, 31, 1), time_unit=MONTH, every_nth=3)
    assert event == dt(2024, 7, 31, 1)

def test_should_not_skip_short_months():
    event = next_occurrence(now=dt(2024, 5, 31, 10), reference=dt(2024, 5, 31, 9), time_unit=MONTH, every_nth=1)
    assert event == dt(2024, 6, 30, 9)

def test_day_of_month_cap_should_not_move_before_now_1():
    event = next_occurrence(now=dt(2024, 5, 31, 14), reference=dt(2023, 5, 31, 12), time_unit=MONTH, every_nth=1)
    assert event != dt(2024, 5, 31, 12)
    assert event == dt(2026, 6, 30, 12)

def test_day_of_month_cap_should_not_move_before_now_2():
    event = next_occurrence(now=dt(2024, 2, 28, 23), reference=dt(2023, 12, 31, 1), time_unit=MONTH, every_nth=2)
    assert event != dt(2024, 2, 28, 1)
    assert event == dt(2024, 4, 30, 1)

def test_feb_nonleap_year():
    event = next_occurrence(now=dt(2023, 2, 28, 1), reference=dt(2023, 1, 31, 2), time_unit=MONTH, every_nth=1)
    assert event == dt(2023, 2, 28, 2)

def test_feb_leap_year():
    event = next_occurrence(now=dt(2024, 2, 28, 1), reference=dt(2024, 1, 31, 2), time_unit=MONTH, every_nth=1)
    assert event == dt(2024, 2, 29, 2)

def test_strip_seconds():
    event = next_occurrence(now=dt(2024, 11, 1, 1), reference=dt(2024, 2, 1, 2), time_unit=MONTH, every_nth=3)
    assert event == dt(2024, 11, 1, 2)

def reproduce_broken_case_1():
    event = next_occurrence(now=dt(2024, 11, 1, 1), reference=dt(2023, 2, 1, 2), time_unit=MONTH, every_nth=3)
    assert event == dt(2024, 11, 1, 2)

def dt(year, month, day, hour):
    return datetime(year, month, day, hour, 15, 0, 0, tzinfo=TZ)

