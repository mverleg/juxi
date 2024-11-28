from datetime import datetime

from django import template

from django.utils import timezone

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


register = template.Library()
register.filter('short_time', short_time)

