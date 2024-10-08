from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class UserTestCase(TestCase):
    def create_user(self):
        User.objects.create_user(username='testuser', password='testpass123')
    
    def test_create_user(self):
        user = User.objects.get(name='testuser')
        self.assertEqual(user.pk)
        
        
# class UserAuthViewsTest(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username='testuser', password='testpassword')

#     def test_signup_view(self):
#         response = self.client.post(reverse('signup'))
#         self.assertEqual(response.status_code, 200)

#         data = {
#             'username': 'newuser',
#             'password1': 'newpassword',
#             'password2': 'newpassword'
#         }
#         response = self.client.post(reverse('signup'), data)
#         self.assertEqual(response.status_code, 302)
#         self.assertEqual(User.objects.filter(username='newuser').exists(), True)

#     def test_login_view(self):
#         response = self.client.get(reverse('login'))
#         self.assertEqual(response.status_code, 200)

#         data = {
#             'username': 'testuser',
#             'password': 'testpassword'
#         }
#         response = self.client.post(reverse('login'), data)
#         self.assertEqual(response.status_code, 302)
#         self.assertEqual('_auth_user_id' in self.client.session, True)

#     def test_logout_view(self):
#         response = self.client.get(reverse('logout'))
#         self.assertEqual(response.status_code, 302)
#         self.assertEqual('_auth_user_id' not in self.client.session, True)