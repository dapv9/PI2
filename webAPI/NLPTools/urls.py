from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    url(r'^$', views.post_new, name='post_new'),
 	url(r'^list/$', views.post_list, name='post_list'),
	url(r'^(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
	url(r'^id=(?P<pk>[0-9]+).json$', views.post_json, name='post_json'),
	url(r'^edit/(?P<pk>[0-9]+)/$', views.post_edit, name='post_edit'),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)