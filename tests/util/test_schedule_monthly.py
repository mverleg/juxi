
from datetime import datetime
import pytz

from juxi.data.schedule import MONTH
from juxi.util.schedule import next_occurrence

TZ = pytz.timezone("Europe/Amsterdam")

def test_interyear_forward_samemonth():
    event = next_occurrence(now=dt(2024, 11, 1, 1), reference=dt(2024, 2, 1, 2), time_unit=MONTH, every_nth=3)
    assert event == dt(2024, 11, 1, 2)

def test_interyear_forward_samemonth_shorter():
    event = next_occurrence(now=dt(2024, 11, 1, 1), reference=dt(2024, 5, 31, 2), time_unit=MONTH, every_nth=3)
    assert event == dt(2024, 11, 30, 2)

def test_intrayear_forward_samemonth():
    assert False

def test_intrayear_forward_samemonth_shorter():
    assert False

def test_interyear_forward_nextmonth():
    assert False

def test_interyear_forward_nextmonth_shorter():
    assert False

def test_intrayear_forward_nextmonth():
    assert False

def test_intrayear_forward_nextmonth_shorter():
    assert False

def test_interyear_backard_samemonth():
    assert False

def test_interyear_backard_samemonth_shorter():
    assert False

def test_intrayear_backard_samemonth():
    assert False

def test_intrayear_backard_samemonth_shorter():
    assert False

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

def test_leap_year():
    assert False

def test_strip_seconds():
    assert False

def dt(year, month, day, hour):
    return datetime(year, month, day, hour, 0, 0, 0, tzinfo=TZ)


