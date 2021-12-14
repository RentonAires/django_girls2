from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),#caminho para post detalhes
    path('post/new/', views.post_new, name='post_new'),
]