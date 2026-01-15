from django import template
from django.conf import settings

register = template.Library()

@register.inclusion_tag('seo_scripts.html', takes_context=True)
def seo_scripts(context):
    # Safe retrieval of variables
    return {
        'GOOGLE_ANALYTICS_ID': getattr(settings, 'GOOGLE_ANALYTICS_ID', ''),
        'GOOGLE_SITE_VERIFICATION': getattr(settings, 'GOOGLE_SITE_VERIFICATION', ''),
        'GOOGLE_ADSENSE_CLIENT_ID': getattr(settings, 'GOOGLE_ADSENSE_CLIENT_ID', ''),
        'debug': settings.DEBUG,
    }