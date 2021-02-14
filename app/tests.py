from django.test import TestCase
from selenium import webdriver
# Create your tests here.

class FunctionalTestCase(TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        
    def test_thereis_homepage(self):
        self.browser.get('http://127.0.0.1:8000/')
        self.assertIn('Hello',self.browser.page_source)
        
    def tearDown(self):
        self.browser.quit()
        