from django.shortcuts import render
from django.http import JsonResponse
from .forms import ContactForm
from .tasks import send_contact_email

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            
            # Use .delay() for production, .call() for local testing if Redis is off
            send_contact_email.delay(cd['name'], cd['email'], cd['message'])

            # send_contact_email(cd['name'], cd['email'], cd['message'])
            
            # Return JSON success instead of rendering a page
            return JsonResponse({'status': 'success', 'message': 'Your message has been sent successfully!'})
        else:
            # Return errors if form is invalid
            return JsonResponse({'status': 'error', 'errors': dict(form.errors.items())}, status=400)
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})