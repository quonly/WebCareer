from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post,ProductDemo,Book
from .forms import ContactForm
from django.db.models import Q
# Create your views here.
# render(request,path html)
def Homepage(request):
    # variable = Table.objects.method()
    # Query all posts
    all_posts = Post.objects.all() # all is call query set
    
    return render(request,'company/home.html',{'all_posts':all_posts})

def post_detail(request, test): # ref with id must add argument id
    single_post = Post.objects.get(id=test) 
    context = {'data':single_post}
    return render(request,'company/post-detail.html',context)

def about(request):
    data = ProductDemo.objects.all() # objects.all() เป็นการคิวรี่แบบ Django --> SELECT * from company_ProductDemo (SQL)
    context = {'data':data}
    return render(request,'company/about.html',context)

def Product(request):
    data = ProductDemo.objects.all() # objects.all() เป็นการคิวรี่แบบ Django --> SELECT * from company_ProductDemo (SQL)
    context = {'data':data}
    return render(request,'company/product.html',context)

def Contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save to DB
            form.save()
            return redirect("/")
    else:
        form = ContactForm()
    return render(request,'company/contact.html',{
        'form' : form,
    })
    
def search(request):
    # Get the incoming query params
    search_post = request.GET.get('q')
    if search_post:
        posts = Post.objects.filter(Q(title__icontains = search_post))
    else:
        pass
    return render(request,'company/search.html',{
        'posts':posts,
        'search_text': search_post,
    })
    
def addbook(request):
    if request.method == 'POST':
        data = request.POST.copy()
        book_title = data.get('book_title') # name in html
        book_descripton = data.get('book_descripton')
        book_price = data.get('book_price')
        
        newbook = Book()
        newbook.title = book_title
        newbook.description = book_descripton
        newbook.price = float(book_price)
        newbook.save()
        return redirect('/')
    
    return render(request,'company/addbook.html')