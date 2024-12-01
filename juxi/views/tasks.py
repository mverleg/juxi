from django.contrib.messages import warning, info
from django.http import HttpResponseBadRequest

from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.http import require_POST

from juxi.models import TaskSeries, TaskRun, NO_STATUS
from juxi.query.schedule import task_overview


def tasks(request):
    return render(request, 'tasks.html', dict(
        task_overview=task_overview(),
    ))


@require_POST
def task_run(request):
    if 'series_id' not in request.POST:
        return HttpResponseBadRequest(redirect("Missing data about which task to run"))
    serie = TaskSeries.objects.get(id=request.POST['series_id'])
    print(serie)
    run = TaskRun(
        series=serie,
        start_at=timezone.now(),
        triggered_by=request.user,
        code=serie.code_template,
        status=NO_STATUS,
    )
    run.save()
    info(request, f"manually started task for {serie.name} at {run.start_at.strftime('%H:%M:%S')}")
    warning(request, f"(tasks don't actually run yet, but they are saved)")  #TODO @mark: TEMPORARY! REMOVE THIS!
    return redirect(reverse('tasks'))

