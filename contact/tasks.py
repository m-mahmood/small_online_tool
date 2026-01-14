from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_contact_email(name, email, message):
    subject = f"New Contact from {name} - Small Online Tool"
    full_message = f"From: {name} ({email})\n\nMessage:\n{message}"
    
    send_mail(
        subject,
        full_message,
        settings.EMAIL_HOST_USER,
        ['m.mahmood.web@gmail.com'], # admin email
        fail_silently=False,
    )