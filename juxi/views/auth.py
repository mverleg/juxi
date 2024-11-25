from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import logout as user_logout

from juxi.forms.auth import LogoutForm, LoginForm


def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if not form.is_valid():
            raise Exception('invalid login form')
        request.logout(request)
        next = form.cleaned_data['next']
        assert next.startswith('/')  #TODO @mark: better validation
        return redirect(next)
    return render(request, 'login.html', dict(
        form=LogoutForm(initial=dict(
            next=request.GET.get('next', reverse('home'))
        ))
    ))
#TODO @mark: validate that `next` is internal?


def logout(request):
    if request.method == 'POST':
        form = LogoutForm(data=request.POST)
        if not form.is_valid():
            raise Exception('invalid logout form')
        user_logout(request)
        next = form.cleaned_data['next']
        assert next.startswith('/')  #TODO @mark: better validation
        return redirect(next)
    return render(request, 'logout.html', dict(
        form=LogoutForm(initial=dict(
            next=request.GET.get('next', reverse('home'))
        ))
    ))

