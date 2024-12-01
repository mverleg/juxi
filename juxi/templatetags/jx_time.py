from datetime import datetime

from django import template

from django.utils import timezone


SEC_PER_DAY = 24 * 60 * 60

def short_time(when: datetime):
    assert timezone.is_aware(when)
    now = timezone.now()
    if when.year != now.year:
        return when.strftime("%Y-%m-%d")
    if when.month != now.month or when.day != now.day:
        return when.strftime("%m-%d")
    delta = when - now
    if abs(delta.seconds) < 90 * 60:
        return when.strftime("%H:%M:%S")
    return when.strftime("%H:%M")


def time_diff(when: datetime):
    now = timezone.now()
    datetime_delta = when - now
    sec_diff = abs(datetime_delta.total_seconds())
    days_diff = int(sec_diff / SEC_PER_DAY)
    template = 'in {} {}' if when > now else '{} {} ago'
    if days_diff > 365 * 2:
        return _fmt(template, days_diff / 365, 'year')
    if days_diff > 30 * 3:
        return _fmt(template, days_diff / 30, 'month')
    if days_diff > 10:
        return _fmt(template, days_diff / 7, 'week')
    if days_diff > 2:
        return _fmt(template, days_diff, 'day')
    if sec_diff > 2 * 60 * 60:
        return _fmt(template, sec_diff / (60 * 60), 'hour')
    if sec_diff > 5 * 60:
        return _fmt(template, sec_diff / 60, 'minute')
    if sec_diff > 10:
        return _fmt(template, sec_diff, 'second')
    return 'now'


def _fmt(template, nr, unit):
    return template.format(round(nr), unit if nr == 1 else f'{unit}s')



register = template.Library()
register.filter('short_time', short_time)
register.filter('time_diff', time_diff)

