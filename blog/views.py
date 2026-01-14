
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def blog_list(request):
    # Fetch all posts, ordered by latest
    all_posts = Post.objects.all().order_by('-created_at')
    
    # Paginate: 10 posts per page
    paginator = Paginator(all_posts, 10)
    
    # Get the current page number from URL (defaults to 1)
    page_number = request.GET.get('page')
    
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page.
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/list.html', {'posts': posts})

def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/detail.html', {'post': post})