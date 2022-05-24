# blog/views.py
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Category

# CBV 방식
# 블로그 목록 페이지
class PostList(ListView):
    model = Post
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

# 블로그 상세 페이지
class PostDetail(DetailView):
    model = Post

'''
# FBV 방식
def index(request):
    # DB에 쿼리를 날려 원하는 레코드를 가지고 옴
    # .order_by('-pk') : 역순으로 가지고 옴
    posts = Post.objects.all().order_by('-pk')

    return render(
        request,
        'blog/index.html',
        {
            'posts': posts,
        }
    )
'''
'''
def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)
    return render(
        request,
        'blog/single_post_page.html',
        {
            'post': post,
        }
    )
'''