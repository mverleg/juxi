from django.shortcuts import redirect

from juxi.query.schedule import task_overview
from juxi.util.render import render_juxi
from juxi.util.url import reverse_param


def home(request):
    if not request.user.is_authenticated:
        return redirect(reverse_param('login', next=request.get_full_path()))
        #TODO @mark: make this default everywhere
    print(task_overview())
    return render_juxi(request, 'home.html')

