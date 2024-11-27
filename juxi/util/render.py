from sys import stderr

from django.db import connection
from django.shortcuts import render

from django.contrib.messages import warning

#TODO @mark: make sure to always use this
def render_juxi(request, template_name, context=None, **kwargs):
    db_query_count_initial = len(connection.queries)
    resp = render(template_name, request, context=context, **kwargs)
    db_query_count = len(connection.queries) - db_query_count_initial
    if db_query_count > 0:
        stderr.write(f"queries in template! {db_query_count} queries in '{template_name}'\n")
    if request.user.is_staff:
        warning(request, f"previous request did {db_query_count} queries for '{template_name}'\n")
    return resp


