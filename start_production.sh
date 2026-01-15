#!/bin/bash
set -e

# 1. Run Migrations (Database setup)
python manage.py migrate --noinput

# 2. Collect Static Files (Images/CSS)
python manage.py collectstatic --noinput

# 3. Start Celery (Background Task) using Detach
# The '--detach' flag stops Celery from taking over the console immediately
celery -A config worker -l info &

# 4. Start Gunicorn (Web Server) in the Foreground
# This keeps the app "alive" for Render
gunicorn config.wsgi:application