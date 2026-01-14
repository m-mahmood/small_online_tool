from django import forms
from django_recaptcha.fields import ReCaptchaField
from django import forms

class GrassCalculatorForm(forms.Form):
    country = forms.ChoiceField(
        choices=[
            ('USA', 'USA'),
            ('UK', 'UK'),
            ('Canada', 'Canada'),
            ('France', 'France'),
            ('New Zealand', 'New Zealand'),
            ('China', 'China'),
            ('India', 'India'),
            ('Pakistan', 'Pakistan'),
            ('Saudi Arabia', 'Saudi Arabia'),
            ('UAE', 'UAE'),
        ],
        widget=forms.Select(attrs={'class': 'w-full border border-gray-300 rounded p-2'})
    )
    
    quality = forms.ChoiceField(
        choices=[
            ('Budget', 'Budget'),
            ('Average', 'Average'),
            ('Premium', 'Premium'),
        ],
        widget=forms.Select(attrs={'class': 'w-full border border-gray-300 rounded p-2'})
    )
    
    length = forms.FloatField(
        min_value=0.1,
        widget=forms.NumberInput(attrs={'class': 'w-full border border-gray-300 rounded p-2', 'placeholder': 'Enter length in meters'})
    )
    
    width = forms.FloatField(
        min_value=0.1,
        widget=forms.NumberInput(attrs={'class': 'w-full border border-gray-300 rounded p-2', 'placeholder': 'Enter width in meters'})
    )
    
    # Standard Google ReCaptcha
    captcha = ReCaptchaField()