from django.test import TestCase
from django.urls import reverse
from EcoHub.orders.models import Cart
from EcoHub.products.models import Product
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile

User = get_user_model()

class OrdersTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='Testpassword123')
        self.product = Product.objects.create(
            name='Test Product',
            description='This is a test product.',
            price=10.50,
            unit='kg',
            category='fruits',
            user=self.user,
            image=SimpleUploadedFile(
                name='test_image.jpg',
                content=b'test image content',
                content_type='image/jpeg'
            )
        )
        Cart.objects.create(user=self.user, product=self.product, quantity=2)

    def test_cart_view(self):
        self.client.login(username='testuser', password='Testpassword123')
        response = self.client.get(reverse('my_bag'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Product')

