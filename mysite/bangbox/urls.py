from django.conf.urls import patterns, url
from bangbox import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^bang/', views.bang, name='bang'),
    url(r'^login/', views.login, name='login'),
    url(r'^check/', views.login_check, name='check'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^signup_check/', views.signup_check, name='signup_check'),
    url(r'^event_page/', views.event_page, name='event_page'),
    url(r'^participation_page/', views.participation_page, name='participation_page')
)
