from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.core.mail import send_mail
from django.conf import settings

from .forms import ContactForm

@ensure_csrf_cookie
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            
            try:
                # FIX: We now use the actual selected subject.
                # cd['subject'] contains the value (e.g., "Bugs").
                # To get the full text (e.g., "Bugs/Errors Related Query") in the email,
                # it is better to use the full label or pass the raw value.
                # Since forms.py uses short values ('Bugs'), let's map them back or just use the value.
                
                # However, if you want the FULL label (e.g. "Bugs/Errors Related Query") 
                # to appear in the Subject line of the email, we can look it up:
                subject_dict = dict(form.fields['subject'].choices)
                full_subject_label = subject_dict.get(cd['subject'], cd['subject'])

                send_mail(
                    subject=full_subject_label, # This will now show "Bugs/Errors Related Query"
                    message=cd['message'],
                    from_email=cd['email'], 
                    recipient_list=[settings.ADMIN_EMAIL], 
                    fail_silently=False
                )
                
                return JsonResponse({'status': 'success', 'message': 'Your message has been sent successfully!'})
                
            except Exception as e:
                print(f"Email Sending Error: {e}")
                return JsonResponse({'status': 'error', 'message': f'Internal Server Error: {str(e)}'}, status=500)
        else:
            return JsonResponse({'status': 'error', 'errors': dict(form.errors.items())}, status=400)
            
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})