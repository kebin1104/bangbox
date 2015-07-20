from django.conf.urls import patterns, url
from bangbox import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
