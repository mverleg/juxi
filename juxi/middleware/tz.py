import logging
import zoneinfo

import django
from django.utils import timezone


def timezone_cookie_middleware(get_response):
    """
    Relies on javascript snippet that sets the timezone cookie
    Adapted from https://stackoverflow.com/a/73956012
    """

    logger = logging.getLogger(timezone_cookie_middleware.__module__)

    def middleware(request):
        try:
            tzname = request.COOKIES.get('juxi.timezone')
            if tzname:
                logger.debug(f'timezone {django.utils.timezone.get_current_timezone()}')
                timezone.activate(zoneinfo.ZoneInfo(tzname))
            else:
                logger.info(f'no timezone for user "{request.user}" timezone')
                timezone.deactivate()
        except Exception as err:
            if request.user.is_authenticated:
                logger.info(f'problem detecting user "{request.user}" timezone, error {str(err)}')
            timezone.deactivate()

        return get_response(request)

    return middleware


