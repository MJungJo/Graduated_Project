from django.contrib import admin
from .models import Post, Category, Tag

# Register your models here.

admin.site.register(Post)

class CategoryAdmin(admin.ModelAdmin):
    # Category모델이 name 필드에 값 입력시 자동 slug만들어짐
    prepopulated_fields = {'slug':('name',)}

# 태그
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)

