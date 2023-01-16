from django.urls import path
from .views import Homepage, about, Product

urlpatterns = [
    path('', Homepage),
    path('about/', about,name='about'),
    path('product/', Product,name='product')
]
