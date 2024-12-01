from django.shortcuts import redirect, render

from juxi.query.schedule import task_overview
from juxi.util.url import reverse_param


def home(request):
    return render(request, 'home.html', dict(
    ))

