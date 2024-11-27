from urllib.parse import urlparse, urlunparse

from django.http import QueryDict
from django.urls import reverse


def reverse_param(view_name: str, **params):
    url = reverse(view_name)
    params_str = url_add_param(view_name, **params)
    return f'{url}?{params_str}'


def url_add_param(current_url: str, **new_params):
    (scheme, netloc, path, cur_params, query, fragment) = urlparse(current_url)
    query_dict = QueryDict(query).copy()
    for k, v in new_params.items():
        query_dict[k] = v
    query = query_dict.urlencode()
    return urlunparse((scheme, netloc, path, cur_params, query, fragment))


