from django.shortcuts import render, redirect

from juxi.query.schedule import task_overview
from juxi.util.url import reverse_param


def home(request):
    if not request.user.is_authenticated:
        print(reverse_param('login', next=request.get_full_path()))  #TODO @mark: TEMPORARY! REMOVE THIS!
        return redirect(reverse_param('login', next=request.get_full_path()))
        #TODO @mark: make this default everywhere
    print(task_overview())
    return render(request, 'home.html')

