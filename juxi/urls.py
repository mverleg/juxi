
from django.contrib import admin
from django.urls import path

from juxi.views.tasks import tasks
from juxi.views.auth import login, logout
from juxi.views.home import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('tasks/', tasks, name='tasks'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),

]
