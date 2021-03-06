from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from bangbox.models import user, event

from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer

from bangbox.serializers import bangboxEventSerializer
# Create your views here.

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)



def index(request):
    return render(request, 'bangbox/index.html')

def bang(request):
    return render(request, 'bangbox/bang.html')

def login(request):
    return render(request, 'bangbox/login.html')

def signup(request):
    return render(request, 'bangbox/signup.html')

def signup_check(request):

    if request.method == 'POST':
        post_email = request.POST['email']
        post_password = request.POST['password']
        post_name = 'bang'

        data = Bangbox_user(email=post_email, name=post_name, password=post_password)
        data.save()

    else:
        return render(request, 'bangbox/signup.html')

    return render(request, 'bangbox/login.html')

def event_page(request):
    return render(request, 'bangbox/event_page.html')

def participation_page(request):
    return render(request, 'bangbox/Participation_page.html')

def login_check(request):
    if request.method == 'POST':
        post_email = request.POST['u_email']
        post_password = request.POST['pass']

        data = user.objects.filter(email=post_email
                                   ).filter(password=post_password
                                            ).count()

        if data == 1:
            return render(request, 'bangbox/index.html')
        else:
            return render(request, 'bangbox/bang.html')

    else:
        return HttpResponseRedirect(request, 'bangbox/bang.html')

class eventViewSet(viewsets.ModelViewSet):
    queryset = event.objects.all()
    serializer_class = bangboxEventSerializer

def api_event(request):
    if request.method == 'GET':
        data = event.objects.filter(id=request.GET['id'])
        serialdata = bangboxEventSerializer(data)

        return JSONResponse(serialdata.data)
    else:
        data = event.objects.all()
        serialdata = bangboxEventSerializer(data)

        return JSONResponse(serialdata.data)