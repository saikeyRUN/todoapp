from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views
from .feeds import LatestEntryField

urlpatterns = [
    url(r'^todos/$', login_required(views.index), name='index'),
    url(r'^todos/details/(?P<id>\w{0,50})/$', views.details),
    url(r'^todos/add', views.add, name='add'),
    #url(r'^todos/logout', views.logout_user, name='logout'),
    #url(r'^todos/feeds/$',LatestEntryField()),

    url(r'^$', views.login_user, name='login_user'),
    #url(r'^logout_user/$', views.logout_user, name='logout_user'),


]
