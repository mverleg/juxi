from dataclasses import dataclass
from typing import Optional, List

from django.db import reset_queries, connection
from django.db.models import Min, Max, OuterRef, Subquery

from juxi.models import TaskRun, TaskSeries


@dataclass
class TaskOverview:
    series: TaskSeries
    previous: Optional[TaskRun]
    next: TaskRun


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

    reset_queries()  #TODO @mark: TEMPORARY! REMOVE THIS!

    subquery = TaskRun.objects.filter(
        series_id=OuterRef('series_id')
    ).values('series_id').annotate(
        max_end_at=Max('end_at')
    ).values('max_end_at')

    queryset = TaskRun.objects.filter(
        end_at=Subquery(subquery)
    )

    print(queryset.query)
    print(queryset.all())


    # djq = TaskRun.objects.filter(end_at=TaskRun.objects.values(latest=Max('end_at')).filter(series_id=OuterRef('series_id')))
    # djq = TaskRun.objects.values('series_id').annotate(latest=Max('end_at'))
    # djq = TaskRun.objects.filter(end_at=Subquery(TaskRun.objects.filter(series_id=OuterRef('series_id')).aggregate(Max('end_at'))))
    # print(djq.query)
    # res = djq.all()
    # print('\n'.join(q['sql'] for q in connection.queries))
    # print(res)

    # series = TaskRun.objects \
    #     .values('series_id') \
    #     .annotate(series=Min('series_id'), last_run=Max('start_at'))
    # print(series)
    # print(
    #     TaskRun.objects
    #     .values('series_id')
    #     .annotate(latest_start_at=Max('start_at'))
    #     .all())



