from django.db import models
from tinymce.models import HTMLField

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = HTMLField('Content') # TinyMCE Field (Images inside content go here)
    
    # NEW: Featured Image Field
    featured_image = models.ImageField(upload_to='blog/featured/', blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # Helper to get the URL if image exists
    def get_featured_image_url(self):
        if self.featured_image:
            return self.featured_image.url
        return "/static/img/default-blog.png" # Fallback placeholder if needed