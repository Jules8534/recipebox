from django.shortcuts import render

from news.models import NewsItem, Author

# Create your views here.
def index(request):
    data = NewsItem.objects.all()
    return render(request, 'index.html', {'data': data})

def recipe_detail(request, id):
    recipe = NewsItem.objects.filter(id=id).first()
    return render(request, 'recipe_detail.html', {'recipe': recipe})

def author_detail(request, id):
    author = Author.objects.filter(id=id).first()
    recipe = NewsItem.objects.filter(author=author)
    return render(request, 'author_detail.html', {'author': author, 'recipe': recipe})


    

    

