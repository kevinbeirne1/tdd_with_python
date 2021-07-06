from django.test import TestCase
from django.urls import resolve

from . import views
from .views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page(self):
        found = resolve("/")
        self.assertEqual(found.func, views.home_page)
