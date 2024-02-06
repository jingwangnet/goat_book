from selenium import webdriver
from django.test import LiveServerTestCase


class NewVisitorTest(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.browser = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    def test_start_to_do_list(self):
        self.browser.get(self.live_server_url)
        self.assertIn("To-Do", self.browser.title)
