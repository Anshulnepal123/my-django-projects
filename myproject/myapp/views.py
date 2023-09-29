from django.core.mail import EmailMultiAlternatives, send_mail
from django.core.paginator import Paginator
from django.shortcuts import HttpResponse, get_object_or_404, redirect, render

from myapp.models import BlogPost, Login

from .forms import *


# Create your views here.
def index(request):
    
    blog = BlogPost.objects.all()
    p = Paginator(blog,2)
    page = request.GET.get('page')
    realpage=p.get_page(page)
    log = Login.objects.all()

    data={
        'blog':blog,
        'blog':realpage,
        'log':log
    }
    
    return render(request,'home.html',data)

def blogdetails(request,blogid):
    blog =BlogPost.objects.get(id=blogid)
    data={
        'blog':blog,
    }
    return render(request,'blogdetails.html',data)

def new_blog(request):
    if request.method == 'POST':
        title=request.POST.get("title")
        content=request.POST.get('content')
        blog = BlogPost(title=title,content=content)
        blog.save()
        return redirect('/')

    return render(request,'new_blog.html')

def old_blog(request):
    blog = BlogPost.objects.all()
    data={
        'blog':blog
    }
    return render(request,'old_blog.html',data)
def contact(request):
    if request.method == 'POST':
        subject = request.POST.get('name')
        from_email = request.POST.get("email")
        msg = request.POST.get('message')
        to= 'nepal.esports.9@gmail.com'
        msg = EmailMultiAlternatives(subject,msg,from_email,[to])
        msg.send()
        return redirect('/')
    return render(request,'contact.html')
def login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get("email")
        password = request.POST.get("password")
        log = Login(name=name,email=email,pw=password)
        log.save()
        return redirect('/')
    

    return render(request,'login.html')

def delete(request,blogid):
    dele = BlogPost.objects.get(id=blogid)
    dele.delete()
    return redirect('old-blog')

def editblog(request,editid):
    pw = get_object_or_404(BlogPost, id=editid)
    
    if request.method == 'POST':
        # Get the data from the submitted form
        new_title = request.POST.get('title')
        new_content = request.POST.get('content')

        # Update the fields in the BlogPost object
        pw.title = new_title
        pw.content = new_content

        # Save the updated object
        pw.save()

        # Redirect to a success page or another appropriate page
        return redirect('/')  # Change the URL as needed

    return render(request, 'update.html', {'id': pw})

