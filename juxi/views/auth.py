
from django.contrib.messages import error, info
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import logout as user_logout, authenticate, login as user_login
from juxi.forms.auth import LogoutForm, LoginForm


def login(request):
    if request.user.is_authenticated:
        return HttpResponseForbidden(redirect("you are already logged in; "
            f"<a href='{reverse('logout')}?next={request.GET.get('next', reverse('home'))}'>logout</a>"))
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is None:
                error(request, "Wrong username or password")
                form.add_error('password', 'Wrong username or password')
            else:
                if not user.is_active:
                    error(request, "Account is disabled")
                    return HttpResponseForbidden(redirect("Account is disabled"))
                info(request, f"Welcome, {user}")
                user_login(request, user)
                next = form.cleaned_data['next']
                assert next.startswith('/')
                return redirect(next)
        else:
            error(request, "Invalid input for username or password")
    else:
        form = LoginForm(initial=dict(
            next=request.GET.get('next', reverse('home'))
        ))
    return render(request, 'login.html', dict(
        form=form,
    ))


def logout(request):
    if request.method == 'POST':
        form = LogoutForm(data=request.POST)
        if not form.is_valid():
            raise Exception('invalid logout form')
        user_logout(request)
        next = form.cleaned_data['next']
        assert next.startswith('/')
        return redirect(next)
    return render(request, 'logout.html', dict(
        form=LogoutForm(initial=dict(
            next=request.GET.get('next', reverse('home'))
        ))
    ))

