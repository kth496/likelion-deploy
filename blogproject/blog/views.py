from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.utils import timezone
from django.shortcuts import redirect

# Create your views here.

def home(request):
    blogs = Blog.objects #쿼리셋
    return render(request, 'home.html', {'blogs' : blogs})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'details': details})

def mainhome(request):
    return render(request, "mainhome.html")

def new(request):
    return render(request, "new.html")

def create(request):
    blog = Blog()
    blog.title = request.POST.get('title',False)
    blog.body = request.POST.get('body', False)
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))