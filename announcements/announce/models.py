from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.template import engines, Context
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
#from announcements import urls

# Models for Pawsey Supercomputing Centre Announcement System.

# Persons responsible for resources
class Owner(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    phone = models.CharField(max_length=18)

    def __unicode__(self):
        return self.name

# Division of the organisation responsible for the resource and the announcement
class Silo(models.Model):
    name = models.CharField(max_length=128)
    owner = models.ForeignKey(Owner)

    def __unicode__(self):
        return self.name

# Physical location of the resources
class Location(models.Model):
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name

# Audiences (email lists, stored as an email address) for the announcements
class Audience(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    maillist = models.EmailField()

    def __unicode__(self):
        return self.name

# Resources available to announce about
class Resource(models.Model):
    name = models.CharField(max_length=128)
    silo = models.ForeignKey(Silo)
    location = models.ForeignKey(Location)
    audience = models.ManyToManyField(Audience)

    def __unicode__(self):
        return self.name

# Template store (in django template language)
class Template(models.Model):
    name = models.CharField(max_length=64)
    html = models.TextField()
    text = models.TextField()

    def __unicode__(self):
        return self.name

# Announcement Store
class Announcement(models.Model):
    subject = models.CharField(max_length=1024)
    reference = models.CharField(max_length=64, unique=True)
    service = models.ManyToManyField(Resource)
    body = models.TextField()
    template = models.ForeignKey(Template)
    dateTimeCreated = models.DateTimeField(auto_now_add=True, editable=False)
    createdBy = models.ForeignKey(User, editable=False, null=True)
    inactive = models.BooleanField(default=False)

    def __unicode__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse('announce:detail', kwargs={'pk': self.pk})

    # Generate list of comma seperated, non repeating, owner for services listed in the announcement.
    def get_serviceowners(self):
        owners = [] 
        for service in self.service.all():
            if not service.silo.owner.name in owners:
                owners.append(str(service.silo.owner.name))
        ownerlist = ', '.join(owners)
        return ownerlist

    # Generate list of comma seperated, non repeating, names for services listed in the announcement.
    def get_servicenames(self):
        names = [] 
        for service in self.service.all():
            if not service.name in names:
                names.append(str(service.name))
        namelist = ', '.join(names)
        return namelist

    # Generate list of comma seperated, non repeating, locations for services listed in the announcement.
    def get_servicelocations(self):
        names = [] 
        for service in self.service.all():
            if not service.location.name in names:
                names.append(str(service.location.name))
        namelist = ', '.join(names)
        return namelist

    # This is the money function. Here we actually send out the announcements to the intended audience. Each audience once.
    def send_email(self):
        django_engine = engines['django']
        html_template = django_engine.from_string(self.template.html)
        text_template = django_engine.from_string(self.template.text)
        
        context = Context({'reference': self.reference, 
            'dateTimeCreated': self.dateTimeCreated, 
            'serviceOwners': self.get_serviceowners(), 
            'serviceNames': self.get_servicenames(), 
            'serviceLocations': self.get_servicelocations(), 
            'body': self.body })

        html_body = html_template.render(context)
        text_body = html_template.render(context)

        subject = self.subject
        from_email = settings.SERVER_EMAIL
        # Create a list of email addresses to send to and avoid any repeats
        to_emails = []
        for service in self.service.all():
            for audience in service.audience.all():
                if not audience.maillist in to_emails:
                    to_emails.append(str(audience.maillist))

        # Send the emails to the destinations as individual emails
        for to in to_emails:
            msg = EmailMultiAlternatives(subject, text_body, from_email, [to])
            msg.attach_alternative(html_body, "text/html")
            msg.send()

        self.inactive=False
        self.save()

# Adding form classes here

# Form for adding and modifying announcements
class AnnouncementForm(ModelForm):
    class Meta:
        model = Announcement
        fields = ['subject', 'reference', 'service', 'template']
