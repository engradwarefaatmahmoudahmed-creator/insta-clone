from django.test import TestCase
from django.urls import reverse

from .models import User

class UserModelTest(TestCase):

 def test_create_user(self):
    user = User.objects.create_user(
        username='testuser',
        email='test@example.com',
        password='testpassword123'
    )

    self.assertEqual(user.username, 'testuser')
    self.assertEqual(user.email, 'test@example.com')
    self.assertTrue(user.check_password('testpassword123'))

 def test_email_is_unique(self):
    User.objects.create_user(
        username='user1',
        email='same@example.com',
        password='password123'
    )

    with self.assertRaises(Exception):
        User.objects.create_user(
            username='user2',
            email='same@example.com',
            password='password123'
        )

 def test_follow_user(self):
    user1 = User.objects.create_user(
        username='user1',
        email='user1@example.com',
        password='password123'
    )

    user2 = User.objects.create_user(
        username='user2',
        email='user2@example.com',
        password='password123'
    )

    user1.following.add(user2)

    self.assertTrue(
        user1.following.filter(id=user2.id).exists()
    )

    self.assertTrue(
        user2.followers.filter(id=user1.id).exists()
    )

 def test_unfollow_user(self):
    user1 = User.objects.create_user(
        username='user1',
        email='user1@example.com',
        password='password123'
    )

    user2 = User.objects.create_user(
        username='user2',
        email='user2@example.com',
        password='password123'
    )

    user1.following.add(user2)
    user1.following.remove(user2)

    self.assertFalse(
        user1.following.filter(id=user2.id).exists()
    )

    self.assertFalse(
        user2.followers.filter(id=user1.id).exists()
    )

class AuthenticationTest(TestCase):

 def setUp(self):
    self.user = User.objects.create_user(
        username='loginuser',
        email='login@example.com',
        password='password123'
    )

 def test_login(self):
    response = self.client.post(
        reverse('login'),
        {
            'username': 'loginuser',
            'password': 'password123'
        }
    )

    self.assertEqual(response.status_code, 302)
    self.assertTrue(
        '_auth_user_id' in self.client.session
    )

 def test_logout(self):
    self.client.login(
        username='loginuser',
        password='password123'
    )

    response = self.client.get(
        reverse('logout')
    )

    self.assertEqual(response.status_code, 302)
    self.assertNotIn(
        '_auth_user_id',
        self.client.session
    )
