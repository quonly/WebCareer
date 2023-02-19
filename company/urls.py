from django.urls import path
from .views import (Homepage, about, Product, post_detail,
                    Contact, search, addbook, sign_in, sign_out)

urlpatterns = [
    path('', Homepage),
    path('about/', about, name='about'),
    path('product/', Product, name='product'),
    # add argument in urls based on parameter in views.py
    path('blog/<int:test>', post_detail),
    path('contact', Contact, name='contact'),
    path('search', search, name='search'),
    path('addbook', addbook, name='addbook'),
    path('sign-in', sign_in, name='sign-in'),
    path('sign-out', sign_out, name='sign-out')
]
