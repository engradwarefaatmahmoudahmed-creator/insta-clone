from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from posts.models import Post
from notifications.models import Notification

from .forms import EditProfileForm, LoginForm, RegisterForm
from .models import User


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')

    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {
        'form': form
    })


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')

    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {
        'form': form
    })


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def profile(request):
    profile_user = request.user

    posts = Post.objects.filter(
        user=profile_user
    ).order_by('-created_at')

    return render(request, 'accounts/profile.html', {
        'profile_user': profile_user,
        'posts': posts,
    })


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(
            request.POST,
            request.FILES,
            instance=request.user
        )

        if form.is_valid():
            form.save()
            return redirect('profile')

    else:
        form = EditProfileForm(instance=request.user)

    return render(request, 'accounts/edit_profile.html', {
        'form': form
    })


@login_required
def user_profile(request, username):
    profile_user = get_object_or_404(
        User,
        username=username
    )

    posts = Post.objects.filter(
        user=profile_user
    ).order_by('-created_at')

    is_following = request.user.following.filter(
        id=profile_user.id
    ).exists()

    return render(request, 'accounts/user_profile.html', {
        'profile_user': profile_user,
        'posts': posts,
        'is_following': is_following,
    })


@login_required
def follow_user(request, username):
    profile_user = get_object_or_404(
        User,
        username=username
    )

    if request.user != profile_user:
        if not request.user.following.filter(
            id=profile_user.id
        ).exists():

            request.user.following.add(profile_user)

            Notification.objects.create(
                recipient=profile_user,
                sender=request.user,
                notification_type='follow'
            )

    return redirect('user_profile', username=username)


@login_required
def unfollow_user(request, username):
    profile_user = get_object_or_404(
        User,
        username=username
    )

    request.user.following.remove(profile_user)

    return redirect('user_profile', username=username)


@login_required
def search_users(request):
    query = request.GET.get('q', '').strip()

    users = User.objects.none()

    if query:
        users = User.objects.filter(
            username__icontains=query
        ).exclude(
            id=request.user.id
        )

    return render(request, 'accounts/search_users.html', {
        'users': users,
        'query': query,
    })