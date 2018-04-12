from django.conf.urls import url
from accounts import views
from lists import views as list_views

urlpatterns = [
    url(r'^send_login_email$', views.send_login_email, name='send_login_email'),
    url(r'^login', views.login, name='login'),
]
