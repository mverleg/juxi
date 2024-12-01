from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List

from django.db import connection
from django.db.models import Max, OuterRef, Subquery
from django.urls import reverse
from django.utils import timezone

from juxi.models import TaskRun, TaskSeries, Schedule
from juxi.util.schedule import next_occurrence


@dataclass
class TaskOverview:
    series: TaskSeries
    schedule: Schedule
    previous: Optional[TaskRun]
    next: datetime

    def series_url(self) -> Optional[str]:
        if self.series is None:
            return None
        return reverse('admin:{}_{}_change'.format(self.series._meta.app_label, self.series._meta.model_name), args=(self.series.pk,))

    def schedule_url(self) -> Optional[str]:
        if self.schedule is None:
            return None
        return reverse('admin:{}_{}_change'.format(self.schedule._meta.app_label, self.schedule._meta.model_name), args=(self.schedule.pk,))

    def previous_url(self) -> Optional[str]:
        if self.previous is None:
            return None
        return reverse('admin:{}_{}_change'.format(self.previous._meta.app_label, self.previous._meta.model_name), args=(self.previous.pk,))


def task_overview() -> List[TaskOverview]:
    # The query we want is this; Django inserts a useless GROUP BY
    # but hopefully the database sees that it's useless and optimizes it
    #   SELECT *
    #   FROM juxi_taskrun AS outr
    #   WHERE outr.start_at = (
    #       SELECT MAX(innr.start_at)
    #       FROM juxi_taskrun AS innr
    #       WHERE outr.series_id == innr.series_id
    #   );

    query_count_init = len(connection.queries)
    all_series = TaskSeries.objects.all()
    all_schedules_map = dict((schedule.id, schedule) for schedule in Schedule.objects.all())
    latest_runs_subquery = (TaskRun.objects.filter(series_id=OuterRef('series_id'))
        .annotate(max_start_at=Max('start_at'))
        .values('max_start_at'))
    latest_runs = (TaskRun.objects
        .filter(start_at=Subquery(latest_runs_subquery))
        .prefetch_related(None)
        .all())
    latest_run_map = dict((run.series_id, run) for run in latest_runs)

    query_count = len(connection.queries) - query_count_init
    assert query_count <= 2
    #TODO @mark: this cannot possibly be passing... ^

    now = timezone.now()
    overview = list(TaskOverview(
        series,
        schedule,
        latest_run_map.get(series.id, None),
        next_occurrence(now, schedule.date_reference, schedule.time_unit, schedule.every_nth),
    ) for series, schedule in [(series, all_schedules_map[series.schedule_id]) for series in all_series])

    return sorted(overview, key=lambda series: series.next)


