from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Post
from .forms import PostForm


def createPost(request):
    form = PostForm
    skills = profile.skill_set.all()
    context = {
        'form' : form,
        }
    return render(request, 'user/createPost.html', context)

