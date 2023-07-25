from django.urls import path

from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.articles_list, name='list'),
    path('category/<slug:slug>/', views.articles_by_category, name='articles_by_category'),
    path('myarticles/', views.articles_user, name='articles_user'),
    path('detail/<int:pk>/', views.articles_detail, name='detail'),
    path('create/', views.articles_create, name='create'),
    path('edit/<int:pk>/', views.articles_edit, name='edit'),
    path('delete/<int:pk>', views.articles_delete, name='delete'),
]
