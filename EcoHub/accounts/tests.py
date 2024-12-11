from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class AccountsTests(TestCase):

    def setUp(self):
        self.user_data = {
            'first_name': 'Test',
            'last_name': 'User',
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'Testpassword123',
            'password2': 'Testpassword123',
        }
        self.login_data = {
            'username': 'testuser',
            'password': 'Testpassword123',
        }
        self.user = User.objects.create_user(
            username='existinguser',
            email='existinguser@example.com',
            password='Testpassword123',
            is_active=True
        )

    def test_user_registration(self):
        response = self.client.post(reverse('register'), self.user_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_user_login(self):
        User.objects.create_user(username='testuser', password='Testpassword123')
        response = self.client.post(reverse('login'), self.login_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue('_auth_user_id' in self.client.session)

    def test_user_logout(self):
        self.client.login(username='existinguser', password='Testpassword123')
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertFalse('_auth_user_id' in self.client.session)

    def test_profile_update(self):
        self.client.login(username='existinguser', password='Testpassword123')
        update_data = {
            'email': 'updatedemail@example.com',
            'phone': '0888123456',
            'address': 'Updated Address',
            'about': 'Updated about section.'
        }
        response = self.client.post(reverse('update_email'), {'email': update_data['email']})
        self.assertEqual(response.status_code, 302)
        self.user.refresh_from_db()
        self.assertEqual(self.user.email, 'updatedemail@example.com')
