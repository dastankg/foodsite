from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


# Create your tests here.

class RegisterUserTestCase(TestCase):

    def setUp(self):
        self.data = {
            'username': 'admin',
            'email': 'astan12324@gmail.com',
            'first_name': 'admin',
            'last_name': 'admin',
            'password1': 'admin',
            'password2': 'admin',

        }

    def test_form_registration_get(self):
        path = reverse('users:register')
        response = self.client.get(path)
        self.assertEquals(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'users/register.html')

    def test_user_registration_success(self):
        user_model = get_user_model()

        path = reverse('users:register')
        response = self.client.post(path, self.data)
        self.assertEquals(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('users:login'))
        self.assertTrue(user_model.objects.filter(username=self.data['username']).exists())

    def test_user_registration_password_error(self):
        self.data['password2'] = 'admin1'

        path = reverse('users:register')
        response = self.client.post(path, self.data)
        self.assertEquals(response.status_code, HTTPStatus.OK)
        self.assertContains(response, 'Пароли не совпадают', html=True)
