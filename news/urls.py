from django.urls import path

from news import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('recipeadd/', views.recipeadd, name="recipe_add"),
    path('authoradd/', views.authoradd, name="author_add"),
    path('recipedetail/<int:id>/', views.recipe_detail, name="recipe_detail"),
    path('author/<int:id>/', views.author_detail, name="author_detail"),
    path('login/', views.loginview, name="login_url"),
    path('logout/', views.logoutview, name="logout_url"),
    path('register/', views.user_create, name="create_url"),
    path('edit/<int:id>/', views.edit_view, name='edit'),
    path('add_favorite/<int:id>/', views.add_favorite, name='favorite'),
    path('unadd_favorite/<int:id>/', views.unadd_favorite, name='unfavorite'),
]
