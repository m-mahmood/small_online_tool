from django import template

register = template.Library()

@register.inclusion_tag('seo_scripts.html', takes_context=True)
def seo_scripts(context):
    request = context['request']
    # Pass variables to the template
    return {
        'GOOGLE_ANALYTICS_ID': context.get('GOOGLE_ANALYTICS_ID'),
        'GOOGLE_SITE_VERIFICATION': context.get('GOOGLE_SITE_VERIFICATION'),
        'GOOGLE_ADSENSE_CLIENT_ID': context.get('GOOGLE_ADSENSE_CLIENT_ID'),
        'DEBUG': context.get('DEBUG', True)
    }