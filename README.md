Pawsey Supercomputing Centre Announcement Management System

This is small Django application to centralise the management for announcements. This is to 
standardise the way that they are delivered and to allow the public to see previous announcements.

Requirements:
Django 1.8 (and it's requirements, including Python 2.7)
Python library for database access, we use PostgreSQL but there is nothing in there that ties us to this particular database system.
django_auth_ldap package for ldap authentication.

Don't edit the settings file directly. Put a pawseyconfig.announcements module somewhere in the pythonpath. Wsgi file has configuration for adding paths.

