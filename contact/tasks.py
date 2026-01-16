from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_contact_email(name, email, subject, message):
    # We pass the full subject label directly from the view if we want, 
    # or reconstruct it. Here we assume the 'subject' passed is the full label.
    
    full_message = f"From: {name} ({email})\n\nMessage:\n{message}"
    
    send_mail(
        subject, # This will be "Bugs/Errors Related Query" (if passed correctly from view)
        full_message,
        settings.EMAIL_HOST_USER,
        [settings.ADMIN_EMAIL], 
        fail_silently=False,
    )