from django.db import models

class Post(models.Model):
    slug = models.SlugField(unique=True)
    image = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    date = models.DateField()
    title = models.CharField(max_length=200)
    excerpt = models.TextField()
    content = models.TextField()

    def __str__(self):
        return self.title