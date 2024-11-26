from django.shortcuts import render, redirect
from django.urls import reverse

from juxi.models import Schedule


def home(request):
    if not request.user.is_authenticated:
        return redirect(f"{reverse('login')}?next={request.get_full_path()}")
        #TODO @mark: make this default everywhere
    Schedule.all().filter(user=request.user)
    return render(request, 'home.html')

