from django.shortcuts import redirect, render

from juxi.query.schedule import task_overview
from juxi.util.url import reverse_param


def tasks(request):
    if not request.user.is_authenticated:
        return redirect(reverse_param('login', next=request.get_full_path()))
        #TODO @mark: make this default everywhere
    return render(request, 'tasks.html', dict(
        task_overview=task_overview(),
    ))

