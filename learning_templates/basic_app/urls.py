from django.urls import path, re_path
from basic_app import views

#TEMPLATE TAGGING
app_name = 'basic_app'

urlpatterns = [
	path('relative/', views.relative, name='relative'),
	#re_path(r'^relative/$', views.relative, name='relative'),
	path('other/', views.other, name='other'),
	#re_path(r'^other/$', views.other, name='other'),
]