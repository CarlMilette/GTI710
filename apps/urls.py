from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^db', views.dbReq, name='dbReq'),
    url(r'^prd', views.prd, name='prd'),


]