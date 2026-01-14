from .models import GeneralPopup

def popup_data(request):
    """
    Fetches active popups and formats them for the base template.
    """
    # Fetch all active popups
    active_popups = GeneralPopup.objects.filter(is_active=True)
    
    # Initialize settings dict
    settings = {
        'enable_adblock_warning': False,
        'enable_exit_intent': False,
        'enable_email_collector': False,
        'email_show_page_path': '',
        'email_delay': 15,
    }

    # Determine current page slug for targeting (e.g., '/grass/' -> 'grass')
    path = request.path
    current_page_slug = path.strip('/').split('/')[0]

    # Detect specific popup types by Name (Case-insensitive)
    # Note: Ensure your Admin entries are named exactly like this, or adjust here.
    for popup in active_popups:
        # 1. AdBlock Warning Check
        if popup.name.lower() == 'adblock warning':
            settings['enable_adblock_warning'] = True

        # 2. Exit Intent Check
        elif popup.name.lower() == 'exit intent':
            settings['enable_exit_intent'] = True

        # 3. Email Collector Check (and targeting logic)
        elif popup.name.lower() == 'email collector':
            settings['enable_email_collector'] = True
            settings['email_show_page_path'] = popup.target_pages or ''
            settings['email_delay'] = popup.delay_seconds

    return {
        'popup_data': active_popups,
        'popups_settings': settings, # This fixes the 'undefined' error in template
        'current_page_slug': current_page_slug
    }