from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.test import Client


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func,home_page)


    def test_home_page_return_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf-8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do</title>',html)
        self.assertTrue(html.endswith,'</html>')
        self.assertTrue(html.strip().endswith('</html>'))


class UrlTest(TestCase):
    def setUp(self) -> None:
        self.c = Client()

    def test_home(self):
        home=self.c.get("http://127.0.0.1:8000/")
        self.assertEqual(home.status_code , 200)