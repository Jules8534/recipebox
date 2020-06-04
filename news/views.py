from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from news.models import NewsItem, Author
from news.forms import NewsAddForm, AuthorAddForm, LoginForm, NewsEditForm


def loginview(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data["username"], password=data["password"]
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get("next", reverse("homepage"))
                )
    form = LoginForm()
    return render(request, "generic_form.html", {"form": form})


def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))


def index(request):
    data = NewsItem.objects.all()
    return render(request, "index.html", {"data": data})


@login_required
def recipeadd(request):
    html = "generic_form.html"

    if request.method == "POST":
        form = NewsAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            NewsItem.objects.create(
                title=data["title"],
                description=data["description"],
                author=data["author"],
            )
            return HttpResponseRedirect(reverse("homepage"))

    form = NewsAddForm()

    return render(request, html, {"form": form})


@login_required
def recipe_edit(request, id):
    """ Allows either the author of a recipe or any staff member to edit
    the shown recipe's title and description.
    """

    recipe = NewsItem.objects.get(id=id)
    form = NewsEditForm(
        initial={"title": recipe.title, "description": recipe.description}
    )
    if request.method == "POST":
        form = NewsEditForm(request.POST)
        if (
            recipe.author.user.username == request.user.username
        ) or request.user.is_staff:
            if request.method == "POST" and form.is_valid():
                data = form.cleaned_data
                recipe.title = data["title"]
                recipe.description = data["description"]
                recipe.save()
            else:
                return render(request, "error.html")

            return HttpResponseRedirect(reverse(recipe_detail, kwargs={"id": id}))
        else:
            return render(request, "error.html")
    return render(request, "generic_form.html", {"form": form},)


def recipe_detail(request, id):
    recipe = NewsItem.objects.filter(id=id).first()
    return render(request, "recipe_detail.html", {"recipe": recipe},)


@login_required
def add_favorite(request, id):
    """ Adds the currently viewed recipe to the list of favorites belonging
    to the currently logged in user.  Unavailable if user isn't logged in. """

    logged_in_user = Author.objects.get(name=request.user.username)
    recipe = NewsItem.objects.get(id=id)
    logged_in_user.favorites.add(recipe)
    logged_in_user.save()

    return HttpResponseRedirect(request.GET.get("next", reverse("homepage")))


def user_create(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            User.objects.create_user(
                username=data["username"], password=data["password"]
            )
            user = authenticate(username=data["username"], password=data["password"])
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get("next", reverse("homepage"))
                )
                return HttpResponseRedirect(reverse("homepage"))

    form = LoginForm()
    return render(request, "generic_form.html", {"form": form})


@login_required
def authoradd(request):
    html = "generic_form.html"
    form = AuthorAddForm()
    if request.method == "POST":
        form = AuthorAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            u = User.objects.create_user(
                username=data["name"], password=data["password"]
            )
            newform = Author.objects.create(name=data["name"], user=u,)

            newform.save()
            return HttpResponseRedirect(reverse("homepage"))

    if request.user.is_staff:
        return render(request, html, {"form": form})

    return render(request, "error.html")


def author_detail(request, id):
    author = Author.objects.filter(id=id).first()
    recipe = NewsItem.objects.filter(author=author)
    favorites = author.favorites.all()
    return render(
        request,
        "author_detail.html",
        {"author": author, "recipe": recipe, "favorites": favorites},
    )
