from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    return render(request, 'bangbox/index.html')

def bang(request):
    return render(request, 'bangbox/bang.html')

def login(request):
    return render(request, 'bangbox/login.html')

def check(request):
    if request.method == 'POST':
        form = NameForm(request.POST)

        if form.is_valid():
            new_name = form.cleaned_data['u_mail']

            return HttpResponseRedirect('bangbox/bang.html')

    else:
        form =NameForm()

    return render(request, 'bangbox/index.html')
