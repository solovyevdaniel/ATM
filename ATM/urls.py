from django.conf.urls import url
from . import views

app_name = 'ATM'
urlpatterns = [
    url(r'^auth/$', views.login, name='login'),
    url(r'^operations/$', views.operations, name='operations'),
    url(r'^$', views.index, name='index'),
]
