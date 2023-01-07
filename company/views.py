from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.
# render(request,path html)
def Homepage(request):
    # variable = Table.objects.method()
    # Query all posts
    all_posts = Post.objects.all()
    
    return render(request,'company/home.html',{'all_posts':all_posts})

def about(request):

    return render(request,'company/about.html')