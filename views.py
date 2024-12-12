from django.shortcuts import render, redirect
from .models import Blog
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import BlogForm
# Create your views here.




def home(request):
    blog = Blog.objects.all()
    users = blog.count()
    context = {'blogs':blog, 'users':users}
    return render(request, 'app/home.html', context)

@login_required(login_url='login') 
def create_post(request):
    if request.method == 'POST':
        text = BlogForm(request.POST)
        if text.is_valid():
            instance =text.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('create')
    else:
        text = BlogForm()
    return render(request, 'app/create.html', {'text':text})

def login_user(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "username doesn't exist!")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'login successful!')
            return redirect('home')
        else:
            messages.error(request, 'invalid username or password!')

    return render(request, 'app/login.html', {'page':page})


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, password=password)
        user.save()
        print('Account was successfully created!')
        return redirect('login')
    return render(request, 'app/signup.html')

def viewing(request, pk):
    view = Blog.objects.get(id=pk)
    context = {
        'view':view
    }
    return render(request, 'app/views.html', context)

def logout_user(request):
    logout(request)
    return redirect('login')


def delete(request, pk):
    obj = Blog.objects.get(id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('home')
    return render(request, 'app/delete.html',{'obj':obj})

def update(request, pk):
    update = Blog.objects.get(id=pk)
    text = BlogForm(instance=update)
    if request.method == 'POST':
        text = BlogForm(request.POST, instance=update)
        if text.is_valid():
            text.save()
            return redirect('home')
    return render(request, 'app/create.html',{'text':text})