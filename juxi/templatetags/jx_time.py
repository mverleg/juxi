from datetime import datetime

from django import template


def short_time(when: datetime):
    now = datetime.now(tz=when.tzinfo)
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

