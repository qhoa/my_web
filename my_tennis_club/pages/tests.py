from django.test import TestCase
from django.urls import reverse
from .models import Post

class test_response(TestCase):
    def test_home_response_status(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    def test_about_response_status(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

class post_model_test(TestCase):
    def setUp(self):
        Post.objects.create(text = 'just a testcase')
    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'just a testcase')

class HomePageViewTest(TestCase): # new

    def setUp(self):
        Post.objects.create(text='this is another test')

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')