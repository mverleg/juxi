from django.shortcuts import redirect, render

from juxi.query.schedule import task_overview
from juxi.util.url import reverse_param


def tasks(request):
    return render(request, 'tasks.html', dict(
        task_overview=task_overview(),
    ))

