from django import template
from django.conf import settings
import os

register = template.Library()

@register.inclusion_tag('seo_scripts.html', takes_context=True)
def seo_scripts(context):
    # 1. Try to get from Settings (loaded from .env)
    # 2. Fallback to Context Processor
    # 3. Fallback to Empty String
    
    verification_id = getattr(settings, 'GOOGLE_SITE_VERIFICATION', context.get('GOOGLE_SITE_VERIFICATION', ''))
    analytics_id = getattr(settings, 'GOOGLE_ANALYTICS_ID', context.get('GOOGLE_ANALYTICS_ID', ''))
    adsense_id = getattr(settings, 'GOOGLE_ADSENSE_CLIENT_ID', context.get('GOOGLE_ADSENSE_CLIENT_ID', ''))
    
    return {
        'GOOGLE_ANALYTICS_ID': analytics_id,
        'GOOGLE_SITE_VERIFICATION': verification_id,
        'GOOGLE_ADSENSE_CLIENT_ID': adsense_id,
        'debug': settings.DEBUG,
    }