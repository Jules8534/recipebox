from django.shortcuts import render, reverse, HttpResponseRedirect

from news.models import NewsItem, Author
from news.forms import NewsAddForm, AuthorAddForm


# Create your views here.
def index(request):
    data = NewsItem.objects.all()
    return render(request, 'index.html', {'data': data})

def recipeadd(request):
    html = "generic_form.html"

    if request.method == "POST":
        form = NewsAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            NewsItem.objects.create(
                title=data['title'],
                description=data['description'],
                author=data['author']
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = NewsAddForm()

    return render(request, html, { 'form': form})


def recipe_detail(request, id):
    recipe = NewsItem.objects.filter(id=id).first()
    return render(request, 'recipe_detail.html', {'recipe': recipe})


def authoradd(request):
    html = "generic_form.html"

    if request.method == "POST":
        form = AuthorAddForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('homepage'))

    form = AuthorAddForm()

    return render(request, html, {'form': form})


def author_detail(request, id):
    author = Author.objects.filter(id=id).first()
    recipe = NewsItem.objects.filter(author=author)
    return render(request, 'author_detail.html', {'author': author, 'recipe': recipe})


    

    

