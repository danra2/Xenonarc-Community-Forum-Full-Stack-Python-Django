from django.conf.urls import url

from django.conf.urls.static import static
from . import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^postmessage$', views.post_message, name="post_message"),
	url(r'^events$', views.events, name="events")
]