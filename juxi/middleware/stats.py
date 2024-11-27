
from time import time

from django.db import connection

PLACEHOLDER = b'%%STATS_PLACEHOLDER%%'


def stats_middleware(get_response):
    """
    Relies on pattern in template: %%STATS_PLACEHOLDER%%
    """

    def middleware(request):
        db_query_count_initial = len(connection.queries)
        page_time_start = time()

        response = get_response(request)

        page_time = 1000 * (time() - page_time_start)
        db_query_count = len(connection.queries) - db_query_count_initial

        if not response or not response.content or response.status_code != 200:
            return None

        if not request.user.is_authenticated:
            response.content = response.content.replace(PLACEHOLDER, '')
            return response

        stat_str = f'time: {page_time:.1f}ms #queries: {db_query_count}'.encode()
        response.content = response.content.replace(PLACEHOLDER, stat_str)
        return response

    return middleware


