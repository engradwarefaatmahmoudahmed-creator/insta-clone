from django import forms

from .models import Comment, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'caption']

        widgets = {
            'caption': forms.Textarea(
                attrs={
                    'placeholder': 'Write a caption...',
                    'rows': 4,
                }
            ),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

        widgets = {
            'text': forms.TextInput(
                attrs={
                    'placeholder': 'Write a comment...',
                }
            ),
        }