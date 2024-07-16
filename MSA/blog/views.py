from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,request
# Create your views here.




def post_detail(request,slug):
    return render(request, "blog/post-detail.html")

def starting_page(request):
    return render(request,"blog/home.html")

def contact(request):
    return render(request,"blog/contact.html")

def about(request):
    return render(request,"blog/about.html")

def blog(request):
    return render(request,"blog/blog.html")

def posts(request):
    return render(request,"blog/all_posts.html")