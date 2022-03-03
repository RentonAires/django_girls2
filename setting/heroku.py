import environ  #carregando a blibioteca eviron

from my_blog.settings.base import * # importanto o setting base para configurar alguma variaveis

env = environ.Env()

DEBUG = env.bool("DEBUG", False)

SECRET_KEY = env("SECRET_KEY") #chave de segurando para deploy

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

DATABASES = {
    "default": env.db(),
}