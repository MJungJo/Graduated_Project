#blog/urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    # CBV방식
    ## 댓글 수정 페이지
    path('update_comment/<int:pk>/', views.CommentUpdate.as_view()),
    ## 포스트 수정 페이지
    path('update_post/<int:pk>/', views.PostUpdate.as_view()),
    ## 포스트 작성 페이지
    path('create_post/', views.PostCreate.as_view()),
    ## 태그 페이지
    path('tag/<str:slug>/', views.tag_page),
    ## 카테고리 페이지
    path('category/<str:slug>/', views.category_page),
    ## CommentForm
    path('<int:pk>/new_comment/', views.new_comment),
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