from django.conf.urls import url
from django.contrib.auth.decorators import login_required, permission_required

from . import views

# List of urls for the announce app. The login required wrappers are stated here as we're using class based views.
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^add/$', login_required(views.AnnouncementCreate.as_view()), name='announcement_add'),
    url(r'^update/(?P<pk>[0-9]+)/$', login_required(views.AnnouncementUpdate.as_view()), name='announcement_update'),
]
