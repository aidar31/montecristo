from django.db import models
from django.urls import reverse
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(unique=True)
    pubdate = models.DateTimeField()
    og_image = models.ImageField(upload_to='images', null=True, blank=True)


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('article_page', kwargs={'slug': self.slug})



