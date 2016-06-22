from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<id>\d+)$', views.index, name = 'my_index'),
    url(r'^message/(?P<id>\d+)$', views.message, name = 'message'),
]