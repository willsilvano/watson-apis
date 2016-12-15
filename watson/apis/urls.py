from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^discover/$', views.discover, name='discover'),
    url(r'^translate/$', views.translate, name='translate'),   
]
