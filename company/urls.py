from django.urls import path
from .views import (Homepage, about, Product, post_detail,Contact,search)

urlpatterns = [
    path('', Homepage),
    path('about/', about,name='about'),
    path('product/', Product,name='product'),
    path('blog/<int:test>',post_detail), # add argument in urls based on parameter in views.py
    path('contact',Contact,name='contact'),
    path('search',search,name='search')
]
