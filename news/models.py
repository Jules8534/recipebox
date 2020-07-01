from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    favorite = models.ManyToManyField("NewsItem", related_name="favorite", blank=True)
    
    def __str__(self):
        return self.name


class NewsItem(models.Model):
    title = models.CharField(max_length=30)
    time_required = models.CharField(max_length=30)
    description = models.TextField()
    instructions = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author =  models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
