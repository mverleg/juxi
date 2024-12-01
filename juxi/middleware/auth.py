from django.shortcuts import redirect

from juxi.util.url import reverse_param


def login_required(get_response):

    def middleware(request):
        if request.path.startswith('/login/'):
            return get_response(request)
        if request.user.is_authenticated:
            return get_response(request)
        return redirect(reverse_param('login', next=request.get_full_path()))

    return middleware
