from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Headline, Review
from ..forms import SignUpForm, ReviewForm
from django.utils import timezone

from newsfeedapp.models import Headline

class TemplateRenderingTestCase(TestCase):
    def test_home_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'newsfeedapp/home.html')

    # Add similar test methods for other templates



    # Add similar test methods for other form submissions

class AuthenticationTestCase(TestCase):
    def test_user_authentication(self):
        user = User.objects.create_user(username='testuser', password='testpassword')  # Create a User instance
        self.client.login(username='testuser', password='testpassword')  # Log in the user
        self.assertIsNotNone(user)
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)  # Adjust status code based on expected behavior

    # Add similar test methods for other authentication-related functionality

class URLAndViewTestCase(TestCase):
    def test_url_resolution(self):
        # Test URL resolution to views
        self.assertEqual(reverse('home'), '/')

    def test_view_functionality(self):
        # Test view functionality
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)  # Adjust status code based on expected behavior
        # Add more assertions to test view functionality

    # Add similar test methods for other URLs and views

class HeadlineModelTestCase(TestCase):
    def setUp(self):
        # Create a sample headline
        self.sample_headline = Headline.objects.create(
            title='Sample Headline',
            description='This is a sample headline description.',
            source_name='Sample Source',
            published_at=timezone.now(),
            url='https://example.com/sample-headline'
        )

    def test_headline_creation(self):
        """Test the creation of a Headline object"""
        headline_count = Headline.objects.count()
        self.assertEqual(headline_count, 1)  # Check if one headline has been created

        headline = Headline.objects.first()
        self.assertEqual(headline.title, 'Sample Headline')  # Check title
        self.assertEqual(headline.description, 'This is a sample headline description.')  # Check description
        self.assertEqual(headline.source_name, 'Sample Source')  # Check source name
        self.assertTrue(headline.published_at)  # Check published date and time
        self.assertEqual(headline.url, 'https://example.com/sample-headline')  # Check URL

    # Add similar test methods for other model creations