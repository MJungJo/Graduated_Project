from .models import Comment
from django import forms

# CommentForm 구현
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)