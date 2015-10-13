from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^upload$', views.upload, name='upload'),
        url(r'^comment$', views.comment, name='comment'),
        url(r'^vote$', views.vote, name='vote'),
    ]
