from django.shortcuts import render, HttpResponseRedirect, reverse
from mooapp.models import Cow
from mooapp.forms import MooForm
import subprocess

def index(request):
    current_moo = Cow.objects.last()
    cmd = ['cowsay', str(current_moo)]
    out = subprocess.check_output(cmd).decode('utf-8')
    if request.method == "POST":
        form = MooForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Cow.objects.create(
                said=data.get('said')
            )
            return HttpResponseRedirect(reverse('home'))
    form = MooForm()
    return render(request, 'index.html', {"form": form, "moo": current_moo, "out": out})

def moos(request):
    main_list = Cow.objects.all()
    moo_list = main_list[0:10]
    return render(request, 'history.html', {"moos": moo_list})