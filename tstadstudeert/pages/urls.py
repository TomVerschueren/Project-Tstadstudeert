from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^nieuws/$', views.nieuws, name='nieuws'),
    url(r'^praktisch/$', views.praktisch, name='praktisch'),
    url(r'^testimonials/$', views.testimonials, name='testimonials'),
    url(r'^links/$', views.links, name='links'),
]