
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

def weird_case_to_check():  #TODO @mark:
    event = next_occurrence(now=dt(2024, 11, 1, 2), reference=dt(2023, 2, 1, 1), time_unit=MONTH, every_nth=3)
    assert event == dt(2024, 11, 1, 1)

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
    assert False

def test_interyear_backard_nextmonth_shorter():
    assert False

def test_intrayear_backard_nextmonth():
    assert False

def test_intrayear_backard_nextmonth_shorter():
    assert False

def test_intrayear_nochange():
    assert False

def test_intrayear_nochange_shorter():
    assert False

def test_pick_shorter_months_when_starting_from_end_of_month():
    #TODO @mark: two cases here:
    # day of month capping should never go before `now`
    # starting on 31st should not skip half the months
    event = next_occurrence(now=dt(2024, 9, 30, 1), reference=dt(2023, 1, 31, 2), time_unit=MONTH, every_nth=3)
    assert event == dt(2024, 9, 30, 1)

def test_feb_nonleap_year():
    event = next_occurrence(now=dt(2023, 2, 28, 1), reference=dt(2023, 1, 31, 2), time_unit=MONTH, every_nth=1)
    assert event == dt(2023, 2, 28, 2)

def test_feb_leap_year():
    event = next_occurrence(now=dt(2024, 2, 28, 1), reference=dt(2024, 1, 31, 2), time_unit=MONTH, every_nth=1)
    assert event == dt(2024, 2, 29, 2)

def test_strip_seconds():
    event = next_occurrence(now=dt(2024, 11, 1, 1), reference=dt(2024, 2, 1, 2), time_unit=MONTH, every_nth=3)
    assert event == dt(2024, 11, 1, 2)

def dt(year, month, day, hour):
    return datetime(year, month, day, hour, 15, 0, 0, tzinfo=TZ)


