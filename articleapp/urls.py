
from django.urls import path

from articleapp.views import ArticleCreateView, ArticleDetailView, ArticleUpdateView, ArticleListView, ArticleDeleteView

app_name='articleapp'

urlpatterns = [
    path('create/', ArticleCreateView.as_view(), name='create'),
    path('delete/<int:pk>/', ArticleDeleteView.as_view(), name='delete'),
    path('detail/<int:pk>/', ArticleDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', ArticleUpdateView.as_view(), name='update'),
    path('list/', ArticleListView.as_view(template_name='articleapp/list.html'), name='list'),
    ]