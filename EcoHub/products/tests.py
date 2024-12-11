from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Product

User = get_user_model()

class ProductsTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='Testpassword123')
        self.product = Product.objects.create(
            name='Existing Product',
            description='This product already exists.',
            price=15.00,
            unit='item',
            category='vegetables',
            user=self.user,
            image=SimpleUploadedFile(name='existing_image.jpg', content=b'existing image content', content_type='image/jpeg')
        )

    def test_product_list_view(self):
        response = self.client.get(reverse('shop'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Existing Product')

    def test_product_detail_view(self):
        response = self.client.get(reverse('shop_detail', args=[self.product.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Existing Product')

    def test_filtering_products_by_price(self):
        response = self.client.get(reverse('shop') + '?min_price=10&max_price=20')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Existing Product')
