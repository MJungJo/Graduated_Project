# blog/views.py
from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    # DB에 쿼리를 날려 원하는 레코드를 가지고 옴
    # .order_by('-pk') : 역순으로 가지고 옴
    posts = Post.objects.all().order_by('-pk')

    return render(
        request,
        'blog/index.html',
        {
            'posts':posts,
        }
    )