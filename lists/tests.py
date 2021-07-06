from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve

from . import views
from .views import home_page


class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "lists/home.html")

