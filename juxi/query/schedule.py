from dataclasses import dataclass
from typing import Optional, List

from django.db import reset_queries, connection
from django.db.models import Min, Max

from juxi.models import TaskRun, TaskSeries


@dataclass
class TaskOverview:
    series: TaskSeries
    previous: Optional[TaskRun]
    next: TaskRun


def task_overview() -> List[TaskOverview]:

    # SELECT *
    # FROM juxi_taskrun AS outr
    # WHERE outr.end_at = (
    #     SELECT MAX(innr.end_at)
    #     FROM juxi_taskrun AS innr
    #     WHERE outr.series_id == innr.series_id
    # );

    reset_queries()
    series = TaskRun.objects \
        .values('series_id') \
        .annotate(series=Min('series_id'), last_run=Max('start_at'))
    print(series)
    print(
        TaskRun.objects
        .values('series_id')
        .annotate(latest_start_at=Max('start_at'))
        .all())

    print('\n'.join(q['sql'] for q in connection.queries))


