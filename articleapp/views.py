from django.shortcuts import render
from django.views.generic import CreateView

from articleapp.forms import ArticleCreationForm
from articleapp.models import NewArticle


# Create your views here.
class ArticleCreateView(CreateView):
    model = NewArticle
    form_class = ArticleCreationForm
    template_name = 'articleapp/create.html'