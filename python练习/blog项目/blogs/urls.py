from django.conf.urls import include,url
import blogs.views as views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # url(r'^index', views.index),
    url(r'^list', views.get_list),
    url(r'^blog', views.get_blog),
    url(r'^login', views.login),
    url(r'^addblog', views.add_blog),
    url(r'^crawler', views.crawler),
    url(r'^delblog', views.del_blog),
    url(r'^editblog', views.edit_blog),
    url(r'^search', views.search),
]