from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.achieved_page, name='achieved_page'),
]
