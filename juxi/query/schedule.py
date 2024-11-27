from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List

from django.db import connection
from django.db.models import Max, OuterRef, Subquery

from juxi.models import TaskRun, TaskSeries, Schedule


@dataclass
class TaskOverview:
    series: TaskSeries
    schedule: Schedule
    previous: Optional[TaskRun]
    next: datetime


def task_overview() -> List[TaskOverview]:
    # The query we want is this; Django inserts a useless GROUP BY
    # but hopefully the database sees that it's useless and optimizes it
    #   SELECT *
    #   FROM juxi_taskrun AS outr
    #   WHERE outr.end_at = (
    #       SELECT MAX(innr.end_at)
    #       FROM juxi_taskrun AS innr
    #       WHERE outr.series_id == innr.series_id
    #   );

    query_count_init = len(connection.queries)
    all_series = TaskSeries.objects.all()
    all_schedules_map = dict((schedule.id, schedule) for schedule in Schedule.objects.all())
    latest_runs_subquery = (TaskRun.objects.filter(series_id=OuterRef('series_id'))
        .annotate(max_end_at=Max('end_at'))
        .values('max_end_at'))
    latest_runs = (TaskRun.objects
        .filter(end_at=Subquery(latest_runs_subquery))
        .prefetch_related(None)
        .all())
    latest_run_map = dict((run.series_id, run) for run in latest_runs)

    query_count = len(connection.queries) - query_count_init
    assert query_count <= 2

    overview = list(TaskOverview(
        series,
        all_schedules_map[series.schedule_id],
        latest_run_map.get(series.id, None),
        datetime.now(),
    ) for series in all_series)

    return sorted(overview, key=lambda series: series.next)


