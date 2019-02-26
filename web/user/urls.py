from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^calendar/$', views.index, name='userIndex'),
    url(r'^settings/$', views.settings, name='userSettings'),
]
