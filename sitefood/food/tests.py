from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from food.models import Food


class GetPagesTestCase(TestCase):
    fixtures = ['food_food.json', 'food_category.json', 'food_tagpost.json']

    def setUp(self):
        pass

    def test_main_page(self):
        path = reverse('home')
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'food/index.html')

    def test_redirect_addpage(self):
        path = reverse('addpage')
        redirect_uri = reverse("users:login") + f"?next={path}"
        response = self.client.get(path)
        self.assertRedirects(response, redirect_uri)



    def test_data_mainpage(self):
        f = Food.published.all().select_related('cat')
        path = reverse('home')
        response = self.client.get(path)
        self.assertQuerySetEqual(response.context_data['posts'], f[:2])


    def test_context_post(self):
        f = Food.published.get(pk=1)
        path = reverse('post', args=[f.slug])
        response = self.client.get(path)
        self.assertEqual(response.context_data['post'], f.content)