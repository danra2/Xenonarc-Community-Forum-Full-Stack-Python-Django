from django.conf.urls import url, include
from . import views

urlpatterns = [

    url(r'^$', views.add_goal, name='add_goal'),
    url(r'^insert_goal$', views.insert_goal, name='insert_goal')
]
