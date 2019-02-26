from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^zombie/$', views.zombie, name='zombie'),
    url(r'^frankenstein/$', views.frankenstein, name='frankenstein'),
    url(r'^voodooDoctor/$', views.voodooDoctor, name='voodooDoctor'),
    url(r'^schedule/$', views.createPageSchedule, name='createPageSchedule'),
    url(r'^book/$', views.book, name='book'),


]
