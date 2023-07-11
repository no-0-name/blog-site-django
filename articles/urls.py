from django.urls import path

from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.articles_list, name='list'),
    path('detail/<int:pk>/', views.articles_detail, name='detail'),
    path('create/', views.articles_create, name='create'),
    path('category/<slug:slug>/', views.articles_by_category, name='articles_by_category')
]
