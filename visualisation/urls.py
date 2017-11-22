from django.conf.urls import patterns, url
from visualisation import views

urlpatterns = patterns('',
        url(r'^client1/$', views.client1, name='client1'),
	url(r'^client2/$', views.client2, name='client2'),
	url(r'^client3/$', views.client3, name='client3')
)
