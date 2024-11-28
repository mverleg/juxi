
from datetime import timedelta

from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone

MONTH = 'month'
WEEK = 'week'
DAY = 'day'
HOUR = 'hour'
MINUTE = 'minute'

UNIT = (
    (MONTH, 'Month'),
    (WEEK, 'Week'),
    (DAY, 'Day'),
    (HOUR, 'Hour'),
    (MINUTE, 'Minute'),
)

def default_time():
    return timezone.now().replace(hour=8, minute=0, second=0, microsecond=0) + timedelta(days=1)


class Schedule(models.Model):
    name = models.CharField(max_length=64, unique=True)
    date_reference = models.DateTimeField(default=default_time)
    time_unit = models.CharField(max_length=8, choices=UNIT, default=UNIT[2])
    every_nth = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name} (every {self.every_nth} {self.time_unit})'


class TaskSeries(models.Model):
    name = models.CharField(max_length=64, unique=True)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    code_template = models.TextField(default="#!/usr/bin/env -S bash -eEu -o pipefail\n\necho 'TODO'")

    def __str__(self):
        return f'{self.name} ({self.schedule.name})'


class TaskRun(models.Model):
    series = models.ForeignKey(TaskSeries, on_delete=models.CASCADE)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    code = models.TextField(blank=True)
    output = models.TextField(blank=True)

    class Meta:
        ordering = ['start_at']

    def __str__(self):
        return f'{self.series.name} at {self.start_at}'

