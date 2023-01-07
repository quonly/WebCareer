from django.urls import path
from .views import Homepage, about

urlpatterns = [
    path('', Homepage),
    path('about', about)
]
