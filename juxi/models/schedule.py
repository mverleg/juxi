
from datetime import timedelta

from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone

from juxi.data.schedule import TIME_UNIT, DAY

NO_STATUS = -1


def default_time():
    return timezone.now().replace(hour=8, minute=0, second=0, microsecond=0) + timedelta(days=1)


class Schedule(models.Model):
    name = models.CharField(max_length=64, unique=True)
    date_reference = models.DateTimeField(default=default_time)
    time_unit = models.CharField(max_length=8, choices=TIME_UNIT, default=DAY)
    every_nth = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])

    class Meta:
        ordering = ['name']

    def save(self, *args, **kwargs):
        self.date_reference = self.date_reference.replace(second=0, microsecond=0)
        super().save(*args, **kwargs)

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
    triggered_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    code = models.TextField(null=True, blank=True)
    output = models.TextField(null=True, blank=True)
    status = models.SmallIntegerField(default=NO_STATUS)

    class Meta:
        ordering = ['start_at']

    def __str__(self):
        return f'{self.series.name} at {self.start_at}'

