from django.test import TestCase
from django.urls import reverse
from EcoHub.reviews.models import Review

class ReviewsTests(TestCase):

    def setUp(self):
        self.review_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'comment': 'Great service!',
            'satisfaction': 5,
        }

        self.low_rating_review = Review.objects.create(
            first_name='Jane',
            last_name='Smith',
            comment='Not satisfied.',
            satisfaction=2
        )

        self.high_rating_review = Review.objects.create(
            first_name='Alice',
            last_name='Brown',
            comment='Excellent experience!',
            satisfaction=5
        )

    def test_create_review(self):
        response = self.client.post(reverse('testimonial'), self.review_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Review.objects.filter(comment='Great service!').exists())

    def test_filter_high_satisfaction_reviews(self):
        response = self.client.get(reverse('testimonial'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Excellent experience!')
        self.assertNotContains(response, 'Not satisfied.')

    def test_review_page_renders(self):
        response = self.client.get(reverse('testimonial'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/testimonial.html')
