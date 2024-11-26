from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse


def home(request):
    if not request.user.is_authenticated:
        return redirect(f"{reverse('login')}?next={request.get_full_path()}")
        #TODO @mark: make this default everywhere
    messages.info(request, f"Welcome, {request.user.username}! (home)")
    return render(request, 'home.html')

