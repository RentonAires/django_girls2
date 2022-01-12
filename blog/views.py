#from django.shortcuts import render
from django.utils import timezone #importe
from .models import Post #importe
from django.shortcuts import render, get_object_or_404, redirect #importe para redirecionar para view
from .forms import PostForm


# Create your views here.

def post_list(request): 
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') #queryset
    return render(request, 'blog/post_list.html', {'posts': posts})

#funcao que retorna o template html
def post_detail(request, pk): 
    post = get_object_or_404(Post, pk=pk) #queryset
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":#condiçao para preencer o fromulario
        form = PostForm(request.POST)#indica que estamo usando para enviado dados 
        if form.is_valid(): #validando o formularios
            post = form.save(commit=False)#salva mas nao cria o objeto
            post.author = request.user#salvando usuario atula 
            post.published_date = timezone.now()#slava com data e hora atual
            post.save() #salvando tudo!!!
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html',{'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
        return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})





