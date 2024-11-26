from dataclasses import dataclass
from typing import Optional, List

from django.db.models import Min, Max

from juxi.models import TaskRun, TaskSeries


@dataclass
class TaskOverview:
    series: TaskSeries
    previous: Optional[TaskRun]
    next: TaskRun


def task_overview() -> List[TaskOverview]:
    series = TaskRun.objects.all()\
        .values('series')\
        .aggregate(lowest=Min('start_at'), highest=Max('start_at'))
    print(series)

