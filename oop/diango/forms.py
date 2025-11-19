"""
表单
"""
from django import forms

from oop.diango.models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        # 我们只让用户填写 body
        # article 和 author 将在视图中自动设置
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add your comment...'}),
        }