
from django.contrib import admin
from django.urls import path

from juxi.views.auth import login, logout
from juxi.views.home import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),

]
