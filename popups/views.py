from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Subscriber, GeneralPopup

def home(request):
    """
    Admin Dashboard for managing popups.
    """
    popups = GeneralPopup.objects.all()
    return render(request, 'popups/admin.html', {'popups': popups})

@require_POST
def process_subscription(request):
    """
    Processes email submission from popup forms.
    """
    email = request.POST.get('email')
    name = request.POST.get('name')
    popup_id = request.POST.get('popup_id') # Identify which popup sent this
    
    try:
        Subscriber.objects.create(email=email, name=name, source='popup_form')
        return JsonResponse({'status': 'success', 'message': 'Thank you! Subscribed successfully.'})
    except Exception:
        return JsonResponse({
            'status': 'error', 
            'message': 'Something went wrong.'
        })