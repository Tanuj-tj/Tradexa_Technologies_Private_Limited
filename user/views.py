from django.contrib.auth.models import User
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .models import Post
from .forms import PostForm


def loginUser(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get('username = username')
        except:
            print('Username does not exist')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('create_Post')
        else:
            print("Username or password is incorrect")

    return render(request, 'user/login_register.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url="login")
def createPost(request):
    form = PostForm
    posts =  Post.objects.all()
    profile = request.user

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False) 
            message.user = profile
            message.save()
            return redirect('success_Page')

    context = {
        'form' : form,
        'posts':posts,
        }

    return render(request, 'user/createPost.html', context)




def successPage(request):
    posts =  Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'user/success.html', context)