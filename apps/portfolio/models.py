from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from taggit.managers import TaggableManager


# Create your models here.
class Portfolio(models.Model):
    def lorem_default():
        return "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi eos laboriosam et eius."
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null = True, default=lorem_default)
    description = models.CharField(max_length=400, null=True, default=lorem_default)
    brandname = models.CharField(max_length=200, null = True, default=lorem_default)
    brandlogo = models.ImageField(upload_to = 'portfolio/img/', null = True)
    brandtypeface = models.ImageField(upload_to = 'portfolio/img/', null = True)
    brandlink = models.URLField(null=True)
    tags = TaggableManager(blank=True)
    text = models.TextField(null=True, blank=True, default=lorem_default)
    slug = models.SlugField(unique=True)
    published_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __int__(self):
        return self.id