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
        form = request.POST['u_email']

        if form == 'kebin1104@nate.com':
            return HttpResponseRedirect('bangbox/bang.html')

    else:
        return render(request, 'bangbox/index.html')
