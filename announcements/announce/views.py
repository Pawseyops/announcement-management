from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required

from .models import *

# Views for the non-admin (main) part of the app

# Summary list of the last few announcements, meant for public view.
class IndexView(generic.ListView):
    template_name = 'announce/index.html'
    context_object_name = 'latest_announcements_list'

    def get_queryset(self):
        """return the last 5 active Announcements"""
        return Announcement.objects.exclude(inactive=True).order_by('-dateTimeCreated')[:5]

# Detailed view of a particular announcement
class DetailView(generic.DetailView):
    model = Announcement
    queryset = Announcement.objects.exclude(inactive=True)
    context_object_name = 'announcementObject'
    template_name = 'announce/detail.html'
    # Restrict access to view inactive announcements to logged in users only.
    def get_queryset(self):
        if self.request.user.is_authenticated():
            return self.model._default_manager.all()
        else:
            return self.queryset.all()

# Announcement creation form (urls.py restricts this to logged in users)
class AnnouncementCreate(CreateView):
    model = Announcement
    fields = ['subject', 'reference', 'service', 'template', 'body']
    template_name = 'announce/add.html'

# Announcement updating form (urls.py restricts this to logged in users)
class AnnouncementUpdate(UpdateView):
    model = Announcement
    fields = ['subject', 'reference', 'service', 'template', 'body']
    template_name = 'announce/update.html'

