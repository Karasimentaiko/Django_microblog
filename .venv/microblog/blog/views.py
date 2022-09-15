from django.shortcuts import render, redirect
from .models import Post
from blog.forms import CommentForm
from django import forms

# Create your views here.
def frontpage(request):
    posts = Post.objects.all()
    return render(request, 'blog/frontpage.html', {"posts":posts})


def login(request):
    return render(request, 'blog/login.html')

def singin(request):
    return render(request, 'blog/singin.html')

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            
            return redirect("post_detail",slug=post.slug)
    else:
         form = CommentForm() 
      
    return render(request,'blog/post_detail.html', {"post": post, "form": form})
