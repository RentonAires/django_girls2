from django.shortcuts import render
from django.utils import timezone #importe
from .models import Post #importe

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') #queryset
    return render(request, 'blog/post_list.html', {'posts': posts})