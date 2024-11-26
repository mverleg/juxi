from django.shortcuts import render, redirect
from django.urls import reverse

from juxi.query.schedule import task_overview


def home(request):
    if not request.user.is_authenticated:
        return redirect(f"{reverse('login')}?next={request.get_full_path()}")
        #TODO @mark: make this default everywhere
    print(task_overview())
    return render(request, 'home.html')

