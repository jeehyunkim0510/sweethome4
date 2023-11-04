
from django.urls import path

from articleapp.views import ArticleCreateView, ArticleDetailView, ArticleUpdateView, ArticleListView, ArticleDeleteView

app_name='familyjoinapp'

urlpatterns = [
    path('create/', ArticleCreateView.as_view(), name='create'),
    ]