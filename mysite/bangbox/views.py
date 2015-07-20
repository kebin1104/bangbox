from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'bangbox/index.html',
                  context_instance=RequestContext(request))
