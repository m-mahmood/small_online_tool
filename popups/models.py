from django.db import models

class Subscriber(models.Model):
    """Stores email subscribers collected via popups."""
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    source = models.CharField(
        max_length=50, 
        default='manual',
        help_text="Source of subscription (e.g. exit_intent, manual)"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class GeneralPopup(models.Model):
    """
    Manages all popups (AdBlock Warning, Exit Intent, General Email Collector).
    Supports targeting specific pages and toggling specific UI elements.
    """
    name = models.CharField(max_length=200, help_text="Name of the popup (Internal Use)")
    
    # --- Configuration ---
    is_active = models.BooleanField(default=True, help_text="Is this popup currently active?")
    
    # --- Trigger Settings ---
    # 1. Target Pages (e.g., 'grass' shows popup on Grass Calc page)
    #    Can be comma-separated: 'grass,bark,tons'
    target_pages = models.CharField(
        max_length=500, 
        blank=True, 
        null=True, 
        help_text="Page slugs (comma separated) to auto-trigger popup. Leave empty to trigger everywhere via timer."
    )
    
    # 2. Timer Settings (For auto-show on target pages)
    delay_seconds = models.PositiveIntegerField(default=15, help_text="Delay in seconds before showing popup on target pages")
    
    # 3. UI Checkmarks (Which elements to show)
    show_checkbox = models.BooleanField(default=False, help_text="Show 'Don't show again' checkbox?")
    show_name = models.BooleanField(default=True, help_text="Show 'Name' input field?")
    show_desc = models.BooleanField(default=True, help_text="Show 'Description' textarea field?")
    
    # --- Content (Shared by all popup types) ---
    # Title
    title = models.CharField(max_length=200, help_text="Popup Title")
    
    # Image
    image = models.ImageField(upload_to='popups/', blank=True, null=True, help_text="Banner image or illustration")
    
    # Links (URL)
    link_url = models.CharField(max_length=200, blank=True, null=True, help_text="URL if clicking image acts as a link")
    
    # HTML Content (Used for Email Collector forms)
    content = models.TextField(blank=True, null=True, help_text="HTML content of the popup body")
    
    # Exit Intent Settings
    is_exit_intent = models.BooleanField(default=False, help_text="If checked, this popup acts as Exit Intent (shows when mouse leaves top)")