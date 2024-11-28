
from juxi.data.schedule import MONTH
from juxi.util.schedule import next_occurrence
from datetime import datetime, timedelta


def test_monthly():
    occ = next_occurrence(now=datetime(2024, 11, 28, 12), reference=datetime(2024, 11, 29, 12), time_unit=MONTH, every_nth=3)
    assert occ == datetime(2024, 11, 29, 12)
