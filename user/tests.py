from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from django.contrib.auth.models import User

class UserRegistrationTestCase(TestCase):
    def test_registration_page_loads(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_user_registration_success(self):
        data = {
            'username': 'testuser',
            'password1': 'strongpassword123',
            'password2': 'strongpassword123',
            'email': 'testuser@example.com'
        }
        response = self.client.post(reverse('register'), data)
        # Assuming successful registration redirects
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_user_registration_password_mismatch(self):
        data = {
            'username': 'testuser2',
            'password1': 'password123',
            'password2': 'password456',
            'email': 'testuser2@example.com'
        }
        response = self.client.post(reverse('register'), data)
        # Should not redirect, should show form again
        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(username='testuser2').exists())

class UserLoginTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='loginuser', password='testpass123')

    def test_login_page_loads(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_user_login_success(self):
        data = {
            'username': 'loginuser',
            'password': 'testpass123'
        }
        response = self.client.post(reverse('login'), data)
        # Assuming successful login redirects
        self.assertEqual(response.status_code, 302)

    def test_user_login_invalid_credentials(self):
        data = {
            'username': 'loginuser',
            'password': 'wrongpassword'
        }
        response = self.client.post(reverse('login'), data)
        # Should not redirect, should show form again
        self.assertEqual(response.status_code, 200)
