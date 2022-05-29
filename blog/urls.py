#blog/urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    # CBV방식
    ## 태그 페이지
    path('tag/<str:slug>/', views.tag_page),
    ## 카테고리 페이지
    path('category/<str:slug>/', views.category_page),
    ## 상세 페이지
    path('<int:pk>/', views.PostDetail.as_view()),
    ## 목록 페이지
    path('', views.PostList.as_view()),


    # FBV 방식
    # 포스트 목록 페이지 정의
    # path('', views.index),

    # 포스트 상세 페이지 URL정의
    # path('<int:pk>/', views.single_post_page),
]