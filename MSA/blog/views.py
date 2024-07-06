from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,request
# Create your views here.




def post_detail(request,post):
    if post == "first":
        return HttpResponse("<h1>this is my first post</h1>")
    elif post == "second":
        return HttpResponse("<h1>this is my second post</h1>")
    else:
        return HttpResponseNotFound("no posts")

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