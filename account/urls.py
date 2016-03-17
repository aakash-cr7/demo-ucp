from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'test_app.views.home', name='home'),
    url(r'^signup/$', 'account.views.signup', name = 'signup'),
    url(r'^login/$', 'account.views.login', name = 'login'),
    url(r'^logout/$', 'account.views.logout', name = 'logout'),
    url(r'^home/$', 'account.views.home', name = 'home'),
    url(r'^verify_email/(?P<uid>\d+)/(?P<token>[0-9A-Za-z_\-]+)/$', 'account.views.verify_email', name='verify_email'),
    url(r'^reset_password/(?P<uid>\d+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 'account.views.reset_password', name='reset_password'),
    url(r'^forgot_password/$', 'account.views.forgot_password', name='forgot_password'),
]
