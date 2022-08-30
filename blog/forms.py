from turtle import title
from django import forms #importa o formulario do django
from .models import Post, Comment #importa o moldelo de post

class PostForm(forms.ModelForm): #informa que vamos usa o padrao de formulario de django
  '''
  title = forms.CharField(
    label='Titulo do Post',
    required=True,
    widget=forms.TextInput
  )

  text = forms.CharField(
    label='digite seu post',
    required=True,
    widget=forms.Textarea
  )'''
  
  class Meta: 
      model = Post #informado ao django que model deve ser usada
      fields = ['title', 'text'] #especificaçao do dos campo

class CommentForm(forms.ModelForm): #informa que vamos usa o padrao de formulario de django
  """
  author = forms.ChoiceField(
    label='Digite seu comentario',
    required=True,
    #widget=forms.ChoiceField
  )"""
  class Meta: 
    model = Comment #informado ao django que model deve ser usada pelo django 
    fields = ('author', 'text',)

        