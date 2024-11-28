
from datetime import timedelta

from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone

NO_STATUS = -1

MONTH = 'month'
WEEK = 'week'
DAY = 'day'
HOUR = 'hour'
MINUTE = 'minute'

TIME_UNIT = (
    (MONTH, 'Month'),
    (WEEK, 'Week'),
    (DAY, 'Day'),
    (HOUR, 'Hour'),
    (MINUTE, 'Minute'),
)
