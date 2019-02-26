from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register/$', views.Register, name='letsRegister'),
    url(r'^login/$', views.Login, name='letsLogin'),
    url(r'^ajax/register/$', views.RegisterAjax, name='letsRegisterAjax'),
    url(r'^ajax/login/$', views.LoginAjax, name='letsLoginAjax'),
    url(r'^logout/$', views.Logout, name='letsLogout'),
    url(r'^authorize/$', views.Authorize, name='letsAuthorize'),
    url(r'^log/the/merchant/in/$', views.MerchantLogin, name='MerchantLogin'),
    url(r'^register/the/merchant/$', views.MerchantRegister, name='MerchantRegister'),
    url(r'^post/a/page/$', views.postAPage, name='postAPage'),
    url(r'^add/a/session/$', views.addSession, name='addSession'),

]
