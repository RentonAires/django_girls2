from django.shortcuts import render
from django.utils import timezone #importe
from .models import Post #importe
from django.shortcuts import render, get_object_or_404

# Create your views here.

def post_list(request): 
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') #queryset
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk): 
    posts = get_object_or_404(Post, pk=pk) #queryset
    return render(request, 'blog/post_detail.html', {'posts': posts})

