#blog/urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    # 포스트 상세 페이지 URL정의
    path('<int:pk>/', views.single_post_page),
    # FBV로 포스트 목록 페이지 정의
    path('', views.index),
]