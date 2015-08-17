#!/bin/sh

VERSION=$1

mkdir /var/www/pythonapps/announcements/$VERSION

git archive --format=tar --prefix=$VERSION/ $VERSION | (cd /var/www/pythonapps/announcements/ && tar xf -)

virtualenv --system-site-packages /var/www/pythonapps/announcements/$VERSION/virtualenv
# Activate virtualenv put these into a requirements file
source /var/www/pythonapps/announcements/$VERSION/virtualenv/bin/activate
pip install django==1.8.3
pip install django_auth_ldap

cd /var/www/pythonapps/announcements/$VERSION
python manage.py collectstatic --noinput
