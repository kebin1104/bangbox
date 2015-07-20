from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'bangbox/index.html')

def bang(request):
    return render(request, 'bangbox/bang.html')

def login(request):
    return render(request, 'bangbox/login.html')
