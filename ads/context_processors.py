from .models import Advertisement

def get_ads(request):
    return {
        'sidebar_top_ad': Advertisement.objects.filter(position='sidebar_top', is_active=True).first(),
        'left_bar_ad': Advertisement.objects.filter(position='left_bar', is_active=True).first(),
        'top_bar_ad': Advertisement.objects.filter(position='top_bar', is_active=True).first(),
        'bottom_bar_ad': Advertisement.objects.filter(position='bottom_bar', is_active=True).first(),
    }