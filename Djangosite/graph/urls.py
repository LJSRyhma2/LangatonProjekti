from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^kosteus/$', views.kosteus, name='kosteus'),
	url(r'^kartta/$', views.kartta, name='kartta'),
]