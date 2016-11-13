from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^db', views.dbReq, name='dbReq'),
    url(r'^prd', views.prd, name='prd'),
    url(r'^venteprd', views.venteprd, name='venteprd'),
    url(r'^ventedate', views.ventedate, name='ventedate'),
    url(r'^ventetot', views.ventetot, name='ventetot'),
    url(r'^ratings', views.RatingList.as_view()),
    url(r'^cmd', views.CommandeList.as_view()),
]