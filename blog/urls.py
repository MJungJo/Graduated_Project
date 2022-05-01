#blog/urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    # CBV방식
    ## 목록 페이지
    path('', views.PostList.as_view()),
    ## 상세 페이지
    path('<int:pk>/', views.PostDetail.as_view()),

    # FBV 방식
    # 포스트 목록 페이지 정의
    # path('', views.index),

    # 포스트 상세 페이지 URL정의
    # path('<int:pk>/', views.single_post_page),
]