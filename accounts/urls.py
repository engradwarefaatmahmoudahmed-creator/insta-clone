from django.urls import path

from .views import (
    edit_profile,
    follow_user,
    login_view,
    logout_view,
    profile,
    register,
    search_users,
    unfollow_user,
    user_profile,
)


urlpatterns = [

    path('register/', register, name='register'),

    path('login/', login_view, name='login'),

    path('logout/', logout_view, name='logout'),

    path('profile/', profile, name='profile'),

    path(
        'profile/edit/',
        edit_profile,
        name='edit_profile'
    ),

    path(
        'user/<str:username>/',
        user_profile,
        name='user_profile'
    ),

    path(
        'user/<str:username>/follow/',
        follow_user,
        name='follow_user'
    ),

    path(
        'user/<str:username>/unfollow/',
        unfollow_user,
        name='unfollow_user'
    ),

    path(
        'search/',
        search_users,
        name='search_users'
    ),

]
