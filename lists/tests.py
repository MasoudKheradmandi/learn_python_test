from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest,HttpResponse
from django.test import Client
from lists.models import Item

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

    def test_home_url(self):
        my_c = self.client.get('/')
        self.assertEqual(my_c.status_code,200)

    def test_obj_and_save(self):
        response=self.client.post('/',data={'my_input':'This test Text'})
        self.assertEqual(Item.objects.count(),1)
        get_item = Item.objects.last()
        self.assertEqual(get_item.text,'This test Text')
        # self.assertEqual(response['location'], '/')

class UrlTest(TestCase):
    def setUp(self) -> None:
        self.c = Client()

    def test_home(self):
        home=self.c.get("http://127.0.0.1:8000/")
        self.assertEqual(home.status_code , 200)

class ListViewTest(TestCase):
    def test_list_view(self):
        Item.objects.create(text="Masoud")
        Item.objects.create(text='ali')
        response=self.client.get('/listview/')
        self.assertContains(response,"Masoud",msg_prefix='indexx')
        self.assertContains(response,'ali')
        