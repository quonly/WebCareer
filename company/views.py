from django.shortcuts import render
from django.http import HttpResponse
from .models import Post,ProductDemo
# Create your views here.
# render(request,path html)
def Homepage(request):
    # variable = Table.objects.method()
    # Query all posts
    all_posts = Post.objects.all()
    
    return render(request,'company/home.html',{'all_posts':all_posts})

def about(request):
    data = ProductDemo.objects.all() # objects.all() เป็นการคิวรี่แบบ Django --> SELECT * from company_ProductDemo (SQL)
    context = {'data':data}
    return render(request,'company/about.html',context)

def Product(request):
    data = ProductDemo.objects.all() # objects.all() เป็นการคิวรี่แบบ Django --> SELECT * from company_ProductDemo (SQL)
    context = {'data':data}
    return render(request,'company/product.html',context)