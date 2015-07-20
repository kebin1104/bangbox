from django.shortcuts import render
from django.templates import RequestContext

# Create your views here.

def index(request):
    return render(request, 'bangbox/index.html',
                  context_instance=RequestContext(request))
