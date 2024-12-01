
from django.contrib import admin

from juxi.models import Schedule, TaskSeries, TaskRun


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['name', 'date_reference', 'time_unit', 'every_nth']
    list_filter = ['time_unit',]


class TaskSeriesAdmin(admin.ModelAdmin):
    list_display = ['name', 'schedule',]
    list_filter = ['schedule',]


class TaskRunAdmin(admin.ModelAdmin):
    list_display = ['id', 'series', 'start_at', 'triggered_by',]
    list_filter = ['series', 'triggered_by',]

    # def has_add_permission(self, request):
    #     return False
    #
    # def has_delete_permission(self, request, obj=None):
    #     return False
    #TODO @mark: make readonly ^

admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(TaskSeries, TaskSeriesAdmin)
admin.site.register(TaskRun, TaskRunAdmin)

