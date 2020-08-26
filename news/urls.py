from django.urls import path

from news import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('recipe_add/', views.recipeadd, name='recipeadd'),
    path('author_add/', views.authoradd, name='authoradd'),
    path("recipedetail/<int:id>/", views.recipe_detail),
    path("author/<int:id>/", views.author_detail),

    # path('admin/', admin.site.urls),
]
