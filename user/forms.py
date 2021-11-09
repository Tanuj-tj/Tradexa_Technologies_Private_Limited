from django.db.models import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from django.forms.models import labels
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['text']
        labels = {
            'text' : 'Post',
        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({ 'class':'input'})