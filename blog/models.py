from django.db import models

# Create your models here.
# 포스트 모델 생성
class Post(models.Model):
    # 제목
    title = models.CharField(max_length=30)
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
    # author = 추후 작성

    def __str__(self):
        # {self.pk} : 해당 포스트의 pk값
        # {self.title} : 해당 포스트의 titler값
        return f'[{self.pk}]{self.title}'

    # 포스트 제목 링크 생성
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'