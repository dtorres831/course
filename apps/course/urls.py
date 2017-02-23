from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^class$', views.blogs),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^delete/remove/(?P<id>\d+)$', views.deletecourse),
    url(r'^user_courses$', views.usercourse)
]
