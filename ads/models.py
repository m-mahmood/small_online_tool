from django.db import models

class Advertisement(models.Model):
    POSITION_CHOICES = [
        ('sidebar_top', 'Sidebar Top'),
        ('left_bar', 'Left Bar (Above Content)'),
        ('top_bar', 'Top Bar (Below Nav)'),
        ('bottom_bar', 'Bottom Bar (Above Footer)'),
    ]

    name = models.CharField(max_length=100)
    position = models.CharField(
        max_length=20, 
        choices=POSITION_CHOICES, 
        unique=True, # Ensure only one active ad per position type
        help_text="Select where this ad will appear on the site."
    )
    image = models.ImageField(upload_to='ads/')
    link = models.URLField(blank=True, null=True, help_text="Optional: URL to open when clicked")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_position_display()} ({self.name})"

    def get_image_url(self):
        if self.image:
            return self.image.url
        return ""