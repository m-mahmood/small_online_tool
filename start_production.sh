#!/bin/bash
set -e

# 1. Migrations
python manage.py migrate --noinput

# 2. Collect Static
python manage.py collectstatic --noinput

# 3. Start Celery (Background)
# The '&& echo' part prevents the script from crashing if Celery has a minor hiccup
celery -A config worker -l info --detach || echo "Celery failed to detach, starting Gunicorn..."

# 4. Start Gunicorn (Web Server)
gunicorn config.wsgi:application