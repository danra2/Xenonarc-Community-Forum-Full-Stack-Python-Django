from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signin$', views.signin, name='signin'),
    url(r'^register$', views.register, name='register'),
    url(r'^validate$', views.validation, name='validation'),
<<<<<<< HEAD
    url(r'^dash$', views.dash, name='dash'),
    url(r'^profile$', views.profile, name='profile'),
    url(r'^editprofile$', views.edit_profile, name='edit_profile'),
    url(r'^editname$', views.edit_name, name='edit_name'),
    url(r'^editemail$', views.edit_email, name='edit_email')
]
=======
    url(r'^success$', views.success, name='success'),
    url(r'^dashboard$', views.dash, name='dashboard'),
]
>>>>>>> 297e82e223fbb9a6e23ca76bdb14b079b128b31d
