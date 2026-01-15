from django.shortcuts import render
from django.http import JsonResponse
from .forms import ContactForm
# Ensure you have this import
from .tasks import send_contact_email

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            
            try:
                # Try to send email synchronously
                send_contact_email(cd['name'], cd['email'], cd['message'])

                # Alternatively, to send email asynchronously using Celery
                # send_contact_email.delay(cd['name'], cd['email'], cd['message'])
                
                # Return Success
                return JsonResponse({'status': 'success', 'message': 'Your message has been sent successfully!'})
                
            except Exception as e:
                # Catch any error (SMTP issues, Server issues) and return them as JSON
                print(f"Email Error: {e}") # This prints to Render logs
                return JsonResponse({'status': 'error', 'message': f'Error sending email: {str(e)}'}, status=500)
        else:
            # Return Form Validation Errors as JSON
            return JsonResponse({'status': 'error', 'errors': dict(form.errors.items())}, status=400)
            
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})