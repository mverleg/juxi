
from django.contrib import admin
from django.urls import path

from juxi.views.home import home
from juxi.views.auth import login, logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('login/', login),
    path('logout/', logout),
]
