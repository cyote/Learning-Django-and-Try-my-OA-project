__author__ = 'apple'

from django.conf.urls import url

from hr import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<user_school_id>[0-9]+)/$', views.school, name='emp_detail')

]