from blog.models import Post

def latest_posts(request):
    """
    Context processor to inject latest blog posts into all templates.
    """
    latest_posts = Post.objects.order_by('-created_at')[:3]
    return {'latest_posts': latest_posts}