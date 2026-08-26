from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CommentForm, PostForm
from .models import Comment, Post
from notifications.models import Notification


@login_required
def home(request):
    following_users = request.user.following.all()

    posts = Post.objects.filter(
        user__in=list(following_users) + [request.user]
    ).order_by('-created_at')

    return render(request, 'posts/home.html', {
        'posts': posts
    })


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            return redirect('home')

    else:
        form = PostForm()

    return render(request, 'posts/create_post.html', {
        'form': form
    })


@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    return render(request, 'posts/post_detail.html', {
        'post': post
    })


@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.user in post.likes.all():
        post.likes.remove(request.user)

    else:
        post.likes.add(request.user)

        if post.user != request.user:
            Notification.objects.create(
                recipient=post.user,
                sender=request.user,
                notification_type='like',
                post=post
            )

    return redirect('home')


@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()

            if post.user != request.user:
                Notification.objects.create(
                    recipient=post.user,
                    sender=request.user,
                    notification_type='comment',
                    post=post
                )

    return redirect('home')


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST' and post.user == request.user:
        post.delete()

    return redirect('home')


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.method == 'POST' and comment.user == request.user:
        comment.delete()

    return redirect('home')
