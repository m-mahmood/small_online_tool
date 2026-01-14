from django.urls import path
from . import views

urlpatterns = [
    path('', views.bark_calculator_view, name='bark-calculator'),
]