from django.urls import path
from . import views

urlpatterns = [
    path('', views.tons_calculator_view, name='tons-calculator'),
]