# chat/urls.py
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^calc_tasks/$', views.calc_tasks, name='calc_tasks'),
    url(r'^create_task/$', views.create_task, name='create_task'),
]
