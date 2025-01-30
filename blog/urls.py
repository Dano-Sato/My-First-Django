from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/new/', views.post_new, name='post_new'),  # ページ 追加
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'), # ページ 削除
]