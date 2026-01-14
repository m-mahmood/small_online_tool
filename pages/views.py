from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')

def privacy(request):
    return render(request, 'pages/privacy.html')

def terms(request):
    return render(request, 'pages/terms.html')

def custom_404(request, exception):
    """
    Custom handler404 to render our template with ads and layout.
    """
    response = render(request, '404.html')
    response.status_code = 404
    return response