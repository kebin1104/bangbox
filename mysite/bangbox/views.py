from django.shortcuts import render
from django.http import HttpResponseRedirect

from bangbox.models import Bangbox_user

# Create your views here.

def index(request):
    return render(request, 'bangbox/index.html')

def bang(request):
    return render(request, 'bangbox/bang.html')

def login(request):
    return render(request, 'bangbox/login.html')

def signup(request):
    return render(request, 'bangbox/signup.html')

def login_check(request):
    if request.method == 'POST':
        post_email = request.POST['u_email']
        post_password = request.POST['pass']

        data = Bangbox_user.objects.filter(email=post_email
                                   ).filter(password=post_password
                                            ).count()

        if data == 1:
            return render(request, 'bangbox/index.html')
        else:
            return render(request, 'bangbox/bang.html')

    else:
        return HttpResponseRedirect(request, 'bangbox/bang.html')
