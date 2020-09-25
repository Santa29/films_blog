from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import CustomUser

# Create your tests here.
class SignUpPageViewTest(TestCase):
    def test_view_signup_url_status_code(self):
        response = self.client.get('/users/signup/')
        self.assertEqual(response.status_code, 200)

    def test_view_signup_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_view_signup_template(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    def test_view_login_confirm_url_status_code(self):
        response = self.client.get('/users/login/')
        self.assertEqual(response.status_code, 200)

    def test_view_login_confirm_url_by_name(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_view_password_reset_confirm_template(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_view_logout_url_status_code(self):
        response = self.client.get('/users/logout/')
        self.assertEqual(response.status_code, 302)

    def test_view_logout_url_by_name(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)

    def test_view_password_change_confirm_url_status_code(self):
        response = self.client.get('/users/password_change/')
        self.assertEqual(response.status_code, 302)

    def test_view_password_change_confirm_url_by_name(self):
        response = self.client.get(reverse('password_change'))
        self.assertEqual(response.status_code, 302)

    def test_view_password_change_confirm_done_url_status_code(self):
        response = self.client.get('/users/password_change/done/')
        self.assertEqual(response.status_code, 302)

    def test_view_password_change_confirm_done_url_by_name(self):
        response = self.client.get(reverse('password_change_done'))
        self.assertEqual(response.status_code, 302)
    
    def test_view_password_reset_confirm_url_status_code(self):
        response = self.client.get('/users/password_reset/')
        self.assertEqual(response.status_code, 200)

    def test_view_password_reset_confirm_url_by_name(self):
        response = self.client.get(reverse('password_reset'))
        self.assertEqual(response.status_code, 200)

    def test_view_password_reset_confirm_done_url_status_code(self):
        response = self.client.get('/users/password_reset/done/')
        self.assertEqual(response.status_code, 200)

    def test_view_password_reset_confirm_done_url_by_name(self):
        response = self.client.get(reverse('password_reset_done'))
        self.assertEqual(response.status_code, 200)