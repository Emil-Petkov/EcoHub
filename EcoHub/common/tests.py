from django.test import TestCase
from django.urls import reverse

class CommonTests(TestCase):

    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_contact_page(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    def test_404_page(self):
        response = self.client.get('/nonexistent/')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404/404.html')