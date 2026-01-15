from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from .forms import ContactForm
from .tasks import send_contact_email

@ensure_csrf_cookie
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            
            try:
                # USE CELERY (delayed task)
                # This puts the task in Redis and returns immediately to the user
                send_contact_email.delay(cd['name'], cd['email'], cd['message'])
                
                return JsonResponse({'status': 'success', 'message': 'Your message has been sent successfully!'})
                
            except Exception as e:
                # This catches connection errors to Redis (e.g., if CELERY_BROKER_URL is missing)
                print(f"Celery/Redis Connection Error: {e}")
                return JsonResponse({'status': 'error', 'message': f'Internal Server Error: {str(e)}'}, status=500)
        else:
            return JsonResponse({'status': 'error', 'errors': dict(form.errors.items())}, status=400)
            
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})