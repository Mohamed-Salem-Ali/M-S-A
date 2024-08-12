from django.db import models
from django.utils.text import slugify
from django.urls import reverse
class Post(models.Model):
    slug = models.SlugField(unique=True, default="",null=False,db_index=True)
    image = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    date = models.DateField()
    title = models.CharField(max_length=200)
    excerpt = models.TextField()
    content = models.TextField()
    
    


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post-detail-page", args=[self.pk])
    
    
    def save(self,*args, **kwargs):
        self.slug=slugify(self.title)
        super().save(*args, **kwargs)
