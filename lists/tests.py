from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page


class HomePageTest(TestCase):
	
	def test_uses_home_template(self):
		response = self.client.get('/')
		
		# it will only work for responses that were retrieved by the test client
		self.assertTemplateUsed(response, 'home.html')

