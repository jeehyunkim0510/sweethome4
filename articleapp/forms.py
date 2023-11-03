from django import forms
from django.forms import ModelForm

from articleapp.models import Article, NewArticle


class ArticleCreationForm(ModelForm):
    class Meta:
        model = Article
        fields=[ 'image', 'content']

class NewArticleCreationForm(ModelForm):
    class Meta:
        model = NewArticle
        fields = ['image', 'content', 'created_at']
        widgets = {
            'created_at': forms.SelectDateWidget()
        }