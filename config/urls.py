from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.http import HttpResponseNotFound
import os
from pages.views import custom_404 

# =============================================================================
# ADS.TXT VIEW (Safe & Optimized)
# =============================================================================

def ads_txt_view(request):
    """
    Serves ads.txt securely from the static folder.
    """
    file_path = os.path.join(settings.BASE_DIR, 'static', 'ads.txt')
    
    if os.path.exists(file_path):
        # Use Django's built-in serve method to handle file locking and headers correctly
        return serve(request, os.path.basename(file_path), os.path.dirname(file_path))
    
    return HttpResponseNotFound("ads.txt file not found.")


# =============================================================================
# URL PATTERNS
# =============================================================================

urlpatterns = [
    path('adminrizq359yxnbp/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    
    # ADS.TXT (Placed here to ensure it is accessible at the root domain.com/ads.txt)
    path('ads.txt', ads_txt_view),
    
    # App Includes
    path('', include('pages.urls')),
    path('blog/', include('blog.urls')),
    path('contact/', include('contact.urls')),
    path('popups/', include('popups.urls')),

    # Tool Endpoints
    path('artificial-grass-calculator/', include('grass_calc.urls')),
    path('bark-calculator/', include('bark_calc.urls')),
    path('tons-to-yards-calculator/', include('tons_calc.urls')),

]

# Static/Media serving
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Custom 404 Handler
handler404 = custom_404