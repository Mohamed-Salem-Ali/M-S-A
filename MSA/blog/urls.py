from django.urls import path , include 
from . import views
urlpatterns = [
    
    path("",views.starting_page, name="starting-page"),
    path("contact",views.contact,name = "contact-page"),
    path("about",views.about,name = "about-page"),
    path("blog",views.blog,name = "blog-page"),
    path("posts",views.posts, name= "posts-page"),
    path("posts/<slug>",views.post_detail,name ="post-detail-page")
]