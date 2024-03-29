from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post_list/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),#caminho para post detalhes
    path('post/new/', views.post_new, name='post_new'),#caminho/view /nome da urls
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('comment/', views.comment, name='comment'),
    
]