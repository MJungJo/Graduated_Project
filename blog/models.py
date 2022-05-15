from django.db import models
from django.contrib.auth.models import User
import os
# Create your models here.
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
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        # {self.pk} : 해당 포스트의 pk값
        # {self.title} : 해당 포스트의 titler값
        return f'[{self.pk}]{self.title} :: {self.author}'

    # 포스트 제목 링크 생성
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'
    # 첨부파일 다운로드
    def get_file_name(self):
        return os.path.basename(self.file_upload.name)
    # 첨부파일 확장자 확인
    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]