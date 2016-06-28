from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^twitter/', include('twitter_app.urls')),
    url(r'^signin$', views.signin, name='signin'),
    url(r'^register$', views.register, name='register'),
    url(r'^validate$', views.validation, name='validation'),
    url(r'^dash$', views.dash, name='dash'),
    url(r'^profile$', views.profile, name='profile'),
    url(r'^editprofile$', views.edit_profile, name='edit_profile')
]