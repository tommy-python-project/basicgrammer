"""
URL 配置
"""
from django.urls import path

from oop.diango.views import ArticleDetailView

urlpatterns = [
    # ... 其他 URL ...
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
]