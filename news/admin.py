from django.contrib import admin

# Register your models here.
from news.models import Author, NewsItem

admin.site.register(Author)
admin.site.register(NewsItem)
