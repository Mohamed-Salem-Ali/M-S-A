from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,request
# Create your views here.

def posts(request,post):
    if post == "first":
        return HttpResponse("<h1>this is my first post</h1>")
    elif post == "second":
        return HttpResponse("<h1>this is my second post</h1>")
    else:
        return HttpResponseNotFound("no posts")


def home(request):
    #context={}
    output = render(request,"home.html")
    return output