from django import forms
from django_recaptcha.fields import ReCaptchaField

# Common styling to match the design
COMMON_WIDGET_ATTRS = {
    'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition'
}

COUNTRIES = ["USA", "UK", "Canada", "France", "New Zealand", "China", "India", "Pakistan", "Saudi Arabia", "UAE"]
QUALITY_CHOICES = [("Budget", "Budget"), ("Average", "Average"), ("Premium", "Premium")]

class BarkCalculatorForm(forms.Form):
    country = forms.ChoiceField(
        choices=[(c, c) for c in COUNTRIES], 
        widget=forms.Select(attrs=COMMON_WIDGET_ATTRS)
    )
    quality = forms.ChoiceField(
        choices=QUALITY_CHOICES,
        initial='Average',
        widget=forms.Select(attrs=COMMON_WIDGET_ATTRS)
    )
    length = forms.FloatField(
        widget=forms.NumberInput(attrs={**COMMON_WIDGET_ATTRS, 'placeholder': 'e.g. 10'})
    )
    width = forms.FloatField(
        widget=forms.NumberInput(attrs={**COMMON_WIDGET_ATTRS, 'placeholder': 'e.g. 5'})
    )
    depth = forms.FloatField(
        widget=forms.NumberInput(attrs={**COMMON_WIDGET_ATTRS, 'placeholder': 'e.g. 5'})
    )
    captcha = ReCaptchaField()