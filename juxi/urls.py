
from django.contrib import admin
from django.template.context_processors import static
from django.urls import path

import settings
from juxi.views.home import home
from juxi.views.auth import login, logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/', login),
    path('logout/', logout),

]
