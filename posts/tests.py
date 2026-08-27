from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from accounts.models import User
from .models import Post, Comment

class PostModelTest(TestCase):

 def create_user(self):
    return User.objects.create_user(
        username='postuser',
        email='post@example.com',
        password='password123'
    )

 def create_image(self, name='test.jpg'):
    return SimpleUploadedFile(
        name=name,
        content=b'fake-image-content',
        content_type='image/jpeg'
    )

 def test_create_post(self):
    user = self.create_user()

    post = Post.objects.create(
        user=user,
        image=self.create_image(),
        caption='My first test post'
    )

    self.assertEqual(post.user, user)
    self.assertEqual(post.caption, 'My first test post')
    self.assertTrue(post.image)

 def test_post_without_caption(self):
    user = self.create_user()

    post = Post.objects.create(
        user=user,
        image=self.create_image('no-caption.jpg')
    )

    self.assertEqual(post.caption, '')
    self.assertEqual(post.user, user)

 def test_post_str(self):
    user = self.create_user()

    post = Post.objects.create(
        user=user,
        image=self.create_image('str.jpg'),
        caption='Test'
    )

    self.assertIn(user.username, str(post))

class CommentModelTest(TestCase):

 def create_user(self):
    return User.objects.create_user(
        username='commentuser',
        email='comment@example.com',
        password='password123'
    )

 def create_post(self, user):
    image = SimpleUploadedFile(
        name='comment.jpg',
        content=b'fake-image-content',
        content_type='image/jpeg'
    )

    return Post.objects.create(
        user=user,
        image=image,
        caption='Test post'
    )

 def test_create_comment(self):
    user = self.create_user()
    post = self.create_post(user)

    comment = Comment.objects.create(
        post=post,
        user=user,
        text='Great post!'
    )

    self.assertEqual(comment.post, post)
    self.assertEqual(comment.user, user)
    self.assertEqual(comment.text, 'Great post!')

 def test_comment_related_to_post(self):
    user = self.create_user()
    post = self.create_post(user)

    comment = Comment.objects.create(
        post=post,
        user=user,
        text='Nice!'
    )

    self.assertIn(comment, post.comments.all())

 def test_comment_str(self):
    user = self.create_user()
    post = self.create_post(user)

    comment = Comment.objects.create(
        post=post,
        user=user,
        text='This is a great post!'
    )

    self.assertIn(user.username, str(comment))
    self.assertIn('This is a great post!', str(comment))

class LikeModelTest(TestCase):

 def create_user(self, username, email):
    return User.objects.create_user(
        username=username,
        email=email,
        password='password123'
    )

 def create_post(self, user):
    image = SimpleUploadedFile(
        name='like.jpg',
        content=b'fake-image-content',
        content_type='image/jpeg'
    )

    return Post.objects.create(
        user=user,
        image=image,
        caption='Like test post'
    )

 def test_like_and_unlike_post(self):
    user = self.create_user(
        'likeuser',
        'like@example.com'
    )

    post = self.create_post(user)

    post.likes.add(user)

    self.assertTrue(
        post.likes.filter(id=user.id).exists()
    )
    self.assertEqual(post.likes.count(), 1)

    post.likes.remove(user)

    self.assertFalse(
        post.likes.filter(id=user.id).exists()
    )
    self.assertEqual(post.likes.count(), 0)

 def test_multiple_users_can_like_post(self):
    owner = self.create_user(
        'owner',
        'owner@example.com'
    )

    user1 = self.create_user(
        'user1',
        'user1@example.com'
    )

    user2 = self.create_user(
        'user2',
        'user2@example.com'
    )

    post = self.create_post(owner)

    post.likes.add(user1)
    post.likes.add(user2)

    self.assertEqual(post.likes.count(), 2)
    self.assertIn(user1, post.likes.all())
    self.assertIn(user2, post.likes.all())
