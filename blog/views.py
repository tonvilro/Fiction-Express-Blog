from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from .models import Post
from django.core.paginator import Paginator
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def home(request):
    if 'my_posts' in request.GET and request.user.is_authenticated:
        posts = Post.objects.filter(author=request.user)
    else:
        posts = Post.objects.all()

    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home.html', {'page_obj': page_obj})

@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Your post has been created!')
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form': form})

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        if request.user == post.author or request.user.is_superuser:
            post.delete()
            messages.success(request, 'Your post has been deleted!')
            return redirect('home')
        else:
            messages.error(request, "You do not have permission to delete this post.")

    return render(request, 'post_confirm_delete.html', {'post': post})