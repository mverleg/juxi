
from django.contrib import admin

from juxi.models import Schedule, TaskSeries, TaskRun


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['name', 'date_reference', 'time_unit', 'every_nth']


class TaskSeriesAdmin(admin.ModelAdmin):
    list_display = ['schedule']


class TaskRunAdmin(admin.ModelAdmin):
    list_display = ['series', 'start_at']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(TaskSeries, TaskSeriesAdmin)
admin.site.register(TaskRun, TaskRunAdmin)

