from django.urls import path

from .views import (
    add_comment,
    create_post,
    delete_comment,
    delete_post,
    home,
    like_post,
    post_detail,
)


urlpatterns = [

    path('', home, name='home'),

    path('create/', create_post, name='create_post'),

    path('post/<int:post_id>/', post_detail, name='post_detail'),

    path(
        'post/<int:post_id>/like/',
        like_post,
        name='like_post'
    ),

    path(
        'post/<int:post_id>/comment/',
        add_comment,
        name='add_comment'
    ),

    path(
        'post/<int:post_id>/delete/',
        delete_post,
        name='delete_post'
    ),

    path(
        'comment/<int:comment_id>/delete/',
        delete_comment,
        name='delete_comment'
    ),

]
