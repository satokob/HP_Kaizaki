from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_view, name='news'),
    path('<int:id>', views.blog_detail, name='blog_detail'),
]
