
from datetime import datetime

from juxi.data.schedule import HOUR, MINUTE
from juxi.util.schedule import next_occurrence
from tests.util.test_schedule_util import TZ


def test_forward_sameday():
    event = next_occurrence(now=tim(10, 12, 30), reference=tim(1, 14, 20), time_unit=MINUTE, every_nth=15)
    assert event == tim(10, 12, 35)

def test_forward_nextday():
    event = next_occurrence(now=tim(2024, 9, 25, 1), reference=tim(2024, 6, 1, 2), time_unit=MINUTE, every_nth=29)
    assert event == tim(2024, 9, 25, 2)
    assert False    #TODO @mark:

def test_backwards_sameday():
    event = next_occurrence(now=tim(2024, 9, 25, 1), reference=tim(2024, 6, 1, 2), time_unit=MINUTE, every_nth=29)
    assert event == tim(2024, 9, 25, 2)
    assert False    #TODO @mark:

def test_backwards_nextday():
    event = next_occurrence(now=tim(2024, 9, 25, 1), reference=tim(2024, 6, 1, 2), time_unit=MINUTE, every_nth=29)
    assert event == tim(2024, 9, 25, 2)
    assert False  #TODO @mark:

def test_hour_same_as_60mins():
    event = next_occurrence(now=tim(2024, 8, 28, 1), reference=tim(2024, 7, 31, 2), time_unit=HOUR, every_nth=1)
    assert event == tim(2024, 8, 28, 2)
    assert False  #TODO @mark:

def test_strip_seconds():
    event = next_occurrence(now=datetime(2024, 11, 1, 1, 55, 20, 30, tzinfo=TZ),
        reference=datetime(2024, 2, 1, 2, 10, 40, 50, tzinfo=TZ), time_unit=MINUTE, every_nth=3)
    assert event.minute == 10
    assert event.second == 0
    assert event.microsecond == 0

def test_very_long():
    event = next_occurrence(now=tim(1971, 1, 15, 2), reference=tim(9999, 12, 31, 4), time_unit=MINUTE, every_nth=1)
    assert event == tim(1971, 1, 15, 4)

def tim(day, hour, minute):
    return datetime(2024, 11, day, hour, minute, 0, 0, tzinfo=TZ)
