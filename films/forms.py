from django.forms import ModelForm
from .models import ReviewComment

class AddCommentForm(ModelForm):
    model = ReviewComment
    fields = ('reviews', )