from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='popup-admin'),
    path('process-subscription/', views.process_subscription, name='process-subscription'),
]