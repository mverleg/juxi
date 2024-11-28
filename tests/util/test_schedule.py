
from datetime import datetime
import pytz

from juxi.data.schedule import MONTH
from juxi.util.schedule import next_occurrence

TZ = pytz.timezone("Europe/Amsterdam")

def test_monthly_tomorrow():
    event = next_occurrence(now=dt(2024, 11, 28, 12), reference=dt(2024, 11, 29, 12), time_unit=MONTH, every_nth=3)
    assert event == dt(2024, 11, 29, 12)

def test_monthly_last_year():
    event = next_occurrence(now=dt(2024, 11, 14, 12), reference=dt(2023, 11 - 6, 13, 0), time_unit=MONTH, every_nth=2)
    assert event == dt(2025, 1, 13, 0)

def test_monthly_future_year():
    event = next_occurrence(now=dt(2024, 11, 28, 12), reference=dt(2026, 6, 15, 10), time_unit=MONTH, every_nth=3)
    assert event == dt(2024, 12, 15, 10)


#TODO @mark: test that seconds/millis can removed

def dt(year, month, day, hour):
    return datetime(year, month, day, hour, 0, 0, 0, tzinfo=TZ)

