from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Form for submitting comments on blog posts.
    This form is used to create or update comments associated with a blog post.
    It includes a single field for the comment body.
    """
    class Meta:
        model = Comment
        fields = ('body',)

        