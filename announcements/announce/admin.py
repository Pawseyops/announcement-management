from django.contrib import admin

from .models import *

# Admin site specific classes.

# Announcement admin fields and actions
class AnnouncementAdmin(admin.ModelAdmin):
    def send_emails(self, request, queryset):
        # do send
        for obj in queryset:
            obj.send_email()

    send_emails.short_description = "Send Announcements Out"

    actions = [send_emails]

# Audience admin list fields
class AudienceAdmin(admin.ModelAdmin):
     list_display = ('name', 'maillist')

# Owner admin list fields
class OwnerAdmin(admin.ModelAdmin):
     list_display = ('name', 'email', 'phone')

# Silo admin list fields
class SiloAdmin(admin.ModelAdmin):
     list_display = ('name', 'owner')

# Resource admin list fields
class ResourceAdmin(admin.ModelAdmin):
     list_display = ('name', 'silo', 'location')

# Register those classes
admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Resource, ResourceAdmin)
admin.site.register(Template)
admin.site.register(Audience, AudienceAdmin)
admin.site.register(Owner, OwnerAdmin)
admin.site.register(Location)
admin.site.register(Silo, SiloAdmin)

# General Site Settings
admin.site.site_header = 'Pawsey Announcement Management System'
admin.site.site_title = 'Pawsey Announcement Management System Administration'
admin.site.index_title = 'Announcement Administration'

