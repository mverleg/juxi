
from django.contrib.auth import logout as user_logout, authenticate, login as user_login
from django.contrib.messages import error, info
from django.http import HttpResponseForbidden, HttpResponseBadRequest
from django.shortcuts import redirect
from django.urls import reverse

from juxi.forms.auth import LogoutForm, LoginForm
from juxi.util.render import render_juxi
from juxi.util.url import reverse_param


def login(request):
    if request.user.is_authenticated:
        next = request.GET.get('next', reverse('home'))
        return HttpResponseForbidden(redirect("you are already logged in; "
            f"<a href='{reverse_param('logout', next=next)}'>logout</a>"))
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
                    return HttpResponseBadRequest(redirect("Account is disabled"))
                user_login(request, user)
                info(request, f"Welcome, {user}")
                next = form.cleaned_data['next']
                assert next.startswith('/')
                return redirect(next)
        else:
            error(request, "Invalid input for username or password")
    else:
        form = LoginForm(initial=dict(
            next=request.GET.get('next', reverse('home'))
        ))
    return render_juxi(request, 'login.html', dict(
        form=form,
    ))


def logout(request):
    if request.method == 'POST':
        form = LogoutForm(data=request.POST)
        if not form.is_valid():
            error(request, "Invalid logout request, did not logout")
            return HttpResponseBadRequest(redirect("Invalid logout request, did not logout"))
        user_logout(request)
        info(request, "Goodbye, you are logged out")
        next = form.cleaned_data['next']
        assert next.startswith('/')
        return redirect(next)
    return render_juxi(request, 'logout.html', dict(
        form=LogoutForm(initial=dict(
            next=request.GET.get('next', reverse('home'))
        ))
    ))

