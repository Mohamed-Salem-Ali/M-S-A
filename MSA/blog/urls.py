from django.urls import path , include
from . import views

urlpatterns = [
    
    path("<post>",views.posts),
    path("",views.home),
    
]