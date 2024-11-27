import logging

from django.contrib.messages import warning
from django.db import connection
from django.shortcuts import render

logger = logging.getLogger(__name__)

#TODO @mark: make sure to always use this
def render_juxi(request, template_name, context=None, **kwargs):
    db_query_count_initial = len(connection.queries)
    resp = render(request, template_name, context=context, **kwargs)
    db_query_count = len(connection.queries) - db_query_count_initial
    if db_query_count > 0:
        example = connection.queries[db_query_count_initial + 1]['sql']
        logger.warning(f"performance warning: {db_query_count} queries in '{template_name}', e.g. {example}\n")
        if request.user.is_staff:
            warning(request, f"previous request did {db_query_count} queries for '{template_name}, e.g. {example}'\n")
    return resp


