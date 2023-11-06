from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.edit import FormMixin, UpdateView, DeleteView

from accountapp.decorators import account_ownership_required
from articleapp.forms import ArticleCreationForm, NewArticleCreationForm
from articleapp.models import NewArticle

has_ownership=[
            login_required,
            account_ownership_required
]
# Create your views here.

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = NewArticle
    form_class = NewArticleCreationForm
    template_name = 'articleapp/create.html'
    success_url = reverse_lazy('homeboardapp:homeboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # 로그인한 사용자 정보
        return kwargs



class ArticleDetailView(LoginRequiredMixin, DetailView, FormMixin):
    model = NewArticle
    form_class = NewArticleCreationForm
    context_object_name = 'target_article'
    template_name = 'articleapp/detail.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # 로그인한 사용자 정보
        return kwargs


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = NewArticle
    form_class = NewArticleCreationForm
    context_object_name = 'target_article'
    template_name = 'articleapp/update.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # 로그인한 사용자 정보
        return kwargs



class ArticleListView(LoginRequiredMixin, ListView):
    model = NewArticle
    context_object_name = 'article_list'
    template_name = 'articleapp/list.html'
    paginate_by = 5

    def get_queryset(self):
        user = self.request.user
        article_list = NewArticle.objects.filter(writer=user).order_by('-created_at')
        return article_list



class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = NewArticle
    context_object_name = 'target_article'
    template_name = 'articleapp/delete.html'
    success_url = reverse_lazy('articleapp:list')

    def get_object(self, queryset=None):
        obj = super().get_object()
        return obj