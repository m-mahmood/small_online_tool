#!/bin/bash
set -e

# 1. Run Migrations
python manage.py migrate --noinput

# 2. Collect Static Files
python manage.py collectstatic --noinput

# 3. Start Celery (Worker) in the Background
# --detach ensures Gunicorn can start afterwards
celery -A config worker -l info --detach

# 4. Start Gunicorn (Web Server) in the Foreground
# This keeps the app "alive"
gunicorn config.wsgi:application