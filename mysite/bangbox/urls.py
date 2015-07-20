from django.conf.urls import patterns, url
from bangbox import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^static/css/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': ROOT_PATH+'/static'}),
)
