from django.contrib import admin
from .models import Subscriber, GeneralPopup

# Admin for Email Subscribers
@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'source', 'created_at')
    list_filter = ('source', 'created_at')
    search_fields = ('email', 'name')
    readonly_fields = ('created_at',)

# Admin for General Popups
@admin.register(GeneralPopup)
class GeneralPopupAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'target_pages', 'delay_seconds')
    list_filter = ('is_active', 'target_pages')
    
    # Organize the form into logical sections
    fieldsets = (
        ('Basic Info', {
            'fields': ('name', 'is_active')
        }),
        ('Triggers', {
            'fields': ('target_pages', 'delay_seconds'),
            'classes': ('collapse',), # Make this collapsible to save space
        }),
        ('UI Elements', {
            'fields': ('show_checkbox', 'show_name', 'show_desc'),
            'classes': ('collapse',),
        }),
        ('Content', {
            'fields': ('title', 'image', 'link_url', 'content'),
            'classes': ('collapse',),
        }),
        ('Exit Intent Mode', {
            'fields': ('is_exit_intent',),
            'classes': ('collapse',),
        }),
    )