from django import forms
from .models import Post, Category, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title',
            'title_tag',
            'author',
            'category',
            'body',
            'snippet',
            'header_image',
        )
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'value': '',
                'id': 'uname',
                'type': 'hidden',
            }),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title',
            'title_tag',
            'category',
            'body',
            'snippet',
        )
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = (
            'name',
        )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'name',
            'body',
        )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
