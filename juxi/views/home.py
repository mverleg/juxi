
from django.shortcuts import render, redirect
from django.urls import reverse


def home(request):
    if not request.user.is_authenticated:
        return redirect(f"{reverse('home')}?next={request.get_full_path()}")
    return render(request, 'home.html')

