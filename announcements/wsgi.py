"""
WSGI config for announcements project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

# Path hackery to make sure all the project's paths appear
# before the system paths in sys.path. addsitedir always
# appends unfortunately.
import site
import sys

webapp_root = os.path.dirname(os.path.abspath(__file__))
oldpath = sys.path[1:]
sys.path = sys.path[:1]
site.addsitedir("~/pawseyconfig")
site.addsitedir(os.path.join(webapp_root,"../virtualenv/lib/python2.7/site-packages"))
site.addsitedir(webapp_root)
sys.path.extend(oldpath)


from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "announcements.settings")

application = get_wsgi_application()
