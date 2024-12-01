
from datetime import datetime
import pytz

from juxi.data.schedule import MONTH
from juxi.util.schedule import next_occurrence

TZ = pytz.timezone("Europe/Amsterdam")

def dt(year, month, day, hour):
    return datetime(year, month, day, hour, 15, 0, 0, tzinfo=TZ)

