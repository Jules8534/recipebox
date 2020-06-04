from django import forms
from news.models import Author


class NewsAddForm(forms.Form):
    title = forms.CharField(max_length=30)
    description = forms.CharField(widget=forms.Textarea)
    author = forms.ModelChoiceField(queryset=Author.objects.all())


class NewsEditForm(forms.Form):
    title = forms.CharField(max_length=30)
    description = forms.CharField(widget=forms.Textarea)


class AuthorAddForm(forms.Form):
    name = forms.CharField(max_length=30)
    bio = forms.CharField(widget=forms.Textarea)
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


"""
class Author(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class NewsItem(models.Model):
    title = models.CharField(max_length=30)
    time_required = models.CharField(max_length=30)
    description = models.TextField()
    instructions = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author =  models.ForeignKey(
        Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
"""
