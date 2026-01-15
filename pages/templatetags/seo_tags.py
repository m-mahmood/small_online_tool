from django import template
from django.conf import settings  # <--- IMPORTANT: Import this

register = template.Library()

@register.inclusion_tag('seo_scripts.html', takes_context=True)
def seo_scripts(context):
    request = context['request']
    return {
        'GOOGLE_ANALYTICS_ID': context.get('GOOGLE_ANALYTICS_ID'),
        'GOOGLE_SITE_VERIFICATION': context.get('GOOGLE_SITE_VERIFICATION'),
        'GOOGLE_ADSENSE_CLIENT_ID': context.get('GOOGLE_ADSENSE_CLIENT_ID'),
        'debug': settings.DEBUG,  # Passes True/False to template
    }