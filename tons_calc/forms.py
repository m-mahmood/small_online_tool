from django import forms
from django_recaptcha.fields import ReCaptchaField

COMMON_WIDGET_ATTRS = {
    'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition'
}

MATERIALS = [
    ("Topsoil (dry)", "Topsoil (dry)"),
    ("Topsoil (wet)", "Topsoil (wet)"),
    ("Garden Soil", "Garden Soil"),
    ("Fill Dirt", "Fill Dirt"),
    ("Sand (dry)", "Sand (dry)"),
    ("Sand (wet)", "Sand (wet)"),
    ("Gravel", "Gravel"),
    ("Crushed Stone", "Crushed Stone"),
    ("Limestone", "Limestone"),
    ("Granite", "Granite"),
    ("Asphalt (millings)", "Asphalt (millings)"),
    ("Concrete (broken)", "Concrete (broken)"),
    ("Clay", "Clay"),
    ("Bark Mulch", "Bark Mulch"),
    ("Wood Mulch", "Wood Mulch"),
    ("Pine Bark", "Pine Bark"),
    ("Compost", "Compost"),
    ("Pea Gravel", "Pea Gravel"),
    ("River Rock", "River Rock"),
    ("Decorative Stone", "Decorative Stone"),
    ("Coal", "Coal"),
    ("Salt", "Salt"),
    ("Gypsum", "Gypsum"),
]

class MaterialConverterForm(forms.Form):
    material = forms.ChoiceField(
        choices=MATERIALS, 
        widget=forms.Select(attrs={**COMMON_WIDGET_ATTRS, 'id': 'id_material'})
    )
    value = forms.FloatField(
        label="Quantity", 
        widget=forms.NumberInput(attrs={**COMMON_WIDGET_ATTRS, 'id': 'id_value', 'placeholder': 'Enter value'})
    )
    density_custom = forms.FloatField(
        required=False, 
        label="Custom Density (Optional)", 
        widget=forms.NumberInput(attrs={**COMMON_WIDGET_ATTRS, 'id': 'id_density_custom', 'placeholder': 'e.g. 1.4'})
    )
    mode = forms.CharField(widget=forms.HiddenInput(attrs={'id': 'id_mode'}), initial='tons_to_yards')
    captcha = ReCaptchaField()