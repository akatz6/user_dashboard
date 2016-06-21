from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'my_index'),
    url(r'^home$', views.index, name = 'my_index'),
    url(r'^login$', views.login, name = 'login'),
    url(r'^register$', views.register, name = 'register'),
    url(r'^add_to_db$', views.add_to_db, name = 'add_to_db'),
    url(r'^validate_password$', views.validate_password, name = 'validate_password'),
    url(r'^remove/(?P<id>\d+)$', views.remove, name = 'remove'),
    url(r'^edit/(?P<id>\d+)$', views.edit, name = 'edit'),
    url(r'^admin_edit/(?P<id>\d+)$', views.admin_edit, name = 'admin_edit'),
    # url(r'^password_edit/(?P<id>\d+)$', views.edit_pass, name = 'edit_pass'),
]