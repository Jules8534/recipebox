from django.urls import path

from news import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('recipeadd/', views.recipeadd),
    path('authoradd/', views.authoradd),
    path("recipedetail/<int:id>/", views.recipe_detail),
    path("author/<int:id>/", views.author_detail),

    # path('admin/', admin.site.urls),
]
