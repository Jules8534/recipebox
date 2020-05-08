from django.urls import path

from news import views

urlpatterns = [
    path('', views.index),
    path("recipedetail/<int:id>/", views.recipe_detail),
    path("author/<int:id>/", views.author_detail),

    # path('admin/', admin.site.urls),
]