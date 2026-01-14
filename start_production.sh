#!/bin/bash

# 1. Run Migrations (to ensure DB is up to date)
echo "Running migrations..."
python manage.py migrate --noinput

# 2. Start Gunicorn (Web Server) AND Celery Worker at the same time
# We use '&' to run them in the background
echo "Starting Gunicorn and Celery..."

# Start Celery in the background
celery -A config worker -l info &

# Start Gunicorn in the foreground (keeps the app alive)
gunicorn config.wsgi:application