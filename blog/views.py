from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Profile, Post, Comment
from .forms import ProfileForm, PostForm, CommentForm
from .blog_deco import create_record, update_record, delete_record


def user_profile(request, pk):
    # Fetch the user
    user = get_object_or_404(User, pk=pk)

    # Fetch the user's profile
    profile = get_object_or_404(Profile, user=user)
    posts = Post.objects.filter(user=pk)

    # Fetch any other related information if necessary

    return render(request, 'user_profile.html',{
        'user': user,
        'profile': profile,
        'posts': posts,
    })


def user_profile_minimal(request, pk):
    # Fetch the user
    user = get_object_or_404(User, pk=pk)

    # Fetch the user's profile
    profile = get_object_or_404(Profile, user=user)
    posts = Post.objects.filter(user=pk)

    # Fetch any other related information if necessary

    return render(request, 'user_profile_minimal.html',{
        'user': user,
        'profile': profile,
        'posts': posts,
    })


# Create Profile
@create_record(Profile, ProfileForm, 'profile_form.html', reverse_lazy('home'))
@login_required
def create_profile(request):
    pass


# Update Profile
@update_record(Profile, ProfileForm, 'profile_form.html', reverse_lazy('home'))
@login_required
def update_profile(request, pk):
    pass


# Delete Profile
@delete_record(Profile, reverse_lazy('home'))
@login_required
def delete_profile(request, pk):
    pass


# Create Post
@create_record(Post, PostForm, 'post_form.html', reverse_lazy('home'))
@login_required
def create_post(request):
    pass


# Update Post
@update_record(Post, PostForm, 'profile_form.html', reverse_lazy('home'))
@login_required
def update_post(request, pk):
    pass


# Delete Post
@delete_record(Post, reverse_lazy('home'))
@login_required
def delete_post(request, pk):
    pass


@login_required
def like_post(request):
    post_id = request.POST.get('post_id')
    post = get_object_or_404(Post, id=post_id)

    if request.user in post.likes.all():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return JsonResponse({
        'liked': liked,
        'like_count': post.likes.count(),
    })


@create_record(Comment, CommentForm, 'comment_form.html', reverse_lazy('home'))
@login_required
def create_comment(request, pk):
    pass