from django.urls import path
from . import views

urlpatterns = [
    path('', views.grass_calculator_view, name='grass-calculator'),
]