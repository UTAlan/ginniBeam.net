from django.forms import ModelForm
from photos.models import Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('author_name','author_email','content')
