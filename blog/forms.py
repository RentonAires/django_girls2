from  django import forms #importa o formulario do django
from .models import Post #importa o moldelo de post

class PostForm(forms.ModelForm): #informa que vamos usa o padrao de formulario de django

    class Meta: 
        model = Post #informado ao django que model deve ser usada pelo django 
        fields = ('title', 'text',) #especificaçao do dos campos 