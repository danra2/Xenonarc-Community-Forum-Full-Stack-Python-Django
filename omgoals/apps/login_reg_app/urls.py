from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signin$', views.signin, name='signin'),
    url(r'^validate$', views.validation, name='validation'),
<<<<<<< HEAD
    url(r'^dashboard$', views.dash, name='dashboard'),
=======
    url(r'^dash$', views.dash, name='dash'),
    url(r'^profile$', views.profile, name='profile'),
    url(r'^editprofile$', views.edit_profile, name='edit_profile'),
    url(r'^editname$', views.edit_name, name='edit_name'),
    url(r'^editemail$', views.edit_email, name='edit_email')
>>>>>>> de30a31e3ee184497d02c72ccc5f688303c05277
]

