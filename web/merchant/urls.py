from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register/$', views.register, name='merchantRegister'),
    url(r'^login/$', views.login, name='merchantLogin'),

    url(r'^$', views.index, name='userIndex'),
    url(r'^pages/$', views.pages, name='userIndex'),
    url(r'^settings/$', views.settings, name='userSettings'),
    url(r'^start/session/(?P<sessionId>[0-9]+)/(?P<pageId>[0-9]+)/$', views.startSession, name='merchantSession'),
]
