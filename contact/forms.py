from django import forms
from django_recaptcha.fields import ReCaptchaField

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:border-sky-500 focus:ring-1 focus:ring-sky-500 outline-none transition'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:border-sky-500 focus:ring-1 focus:ring-sky-500 outline-none transition'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:border-sky-500 focus:ring-1 focus:ring-sky-500 outline-none transition', 'rows': 4})
    )
    captcha = ReCaptchaField()