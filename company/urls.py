from django.urls import path
from .views import (Homepage, about, Product, post_detail,
                    Contact, search, addbook, book)

urlpatterns = [
    path('', Homepage),
    path('about/', about, name='about'),
    path('product/', Product, name='product'),
    # add argument in urls based on parameter in views.py
    path('blog/<int:test>', post_detail),
    path('contact', Contact, name='contact'),
    path('search', search, name='search'),
    path('addbook', addbook, name='addbook'),
    path('book', book, name='book'),
    path('book/delete/<int:id>', book),
    path('book/edit/<int:id>', book),
]
