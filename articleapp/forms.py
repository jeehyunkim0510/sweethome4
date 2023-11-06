from django import forms
from django.contrib.auth.models import User
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

    def __init__(self, user, *args, **kwargs):
        super(NewArticleCreationForm, self).__init__(*args, **kwargs)

        # 기존 필드 제거
        self.fields.pop('writer', None)

        self.fields['writer'] = forms.ModelChoiceField(queryset=User.objects.filter(pk=user.pk), initial=user.pk,
                                                       widget=forms.HiddenInput())

    def save(self, commit=True):
        # 저장 시 writer와 group 정보 추가
        instance = super(NewArticleCreationForm, self).save(commit=False)
        instance.writer = self.cleaned_data['writer']

        if commit:
            instance.save()

        return instance
