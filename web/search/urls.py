from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.launch, name='index'),
    url(r'^preview/$', views.index,name='preview'),
    url(r'^preview/listing/(?P<id>[\w-]+)/$', views.listing, name='listing')
]
