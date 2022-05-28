from django.db import models
from django.contrib.auth.models import User
import os
# Create your models here.

# 태그 모델 생성
class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/tag/{self.slug}'

# 카테고리 모델 생성
class Category(models.Model):
    # 각 카테고리의 이름을 담는 필드(중복 불가)
    name = models.CharField(max_length=50, unique=True)
    # 고유 URL만들 때 사용,(중복 불가)(한글가능)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name
    
    # 카테고리 페이지 작성
    def get_absolute_url(self):
        return f'/blog/category/{self.slug}/'
    
    ## 관리자 페이지의 'Categorys' -> 'Categories'변경
    class Meta:
        verbose_name_plural = 'Categories'

# 포스트 모델 생성
class Post(models.Model):
    # 제목
    title = models.CharField(max_length=30)
    # 요약문 필드 만들기
    hook_text = models.CharField(max_length=100, blank=True)
    # 내용
    content = models.TextField()
    # 이미지
    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    # 파일 업로드
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)

    # 작성일
    ## 자동으로 작성시각, 수정시각 저장하기
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # 작성자 정보
    ## ForeignKey로 author 필드 구현
    ## SET_NULL : 작성자 삭제시 빈 칸으로 둠
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    # 카테고리
    ## null=True : 카테고리 미분류도 있을 수 있기에
    ## on_delete=models.SET_NULL : 카테고리 삭제시 연결된 포스트 삭제 되지 않도록 NUll설정
    ## blank=True : Post모델에 Category없어도 저장 가능하도록 함
    category = models.ForeignKey(Category, null=True,
                                 on_delete=models.SET_NULL,
                                 blank=True)

    # 태그
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        # {self.pk} : 해당 포스트의 pk값
        # {self.title} : 해당 포스트의 titler값
        return f'[{self.pk}]{self.title} :: writer [{self.author}] :: category [{self.category}]'

    # 포스트 제목 링크 생성
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'
    # 첨부파일 다운로드
    def get_file_name(self):
        return os.path.basename(self.file_upload.name)
    # 첨부파일 확장자 확인
    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]