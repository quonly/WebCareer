from django.urls import path
from .views import Homepage, about, Product, post_detail

urlpatterns = [
    path('', Homepage),
    path('about/', about,name='about'),
    path('product/', Product,name='product'),
    path('blog/<int:id>',post_detail) # add argument in urls based on parameter in views.py
]
