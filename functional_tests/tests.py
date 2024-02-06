from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
import time


class NewVisitorTest(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.browser = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    def check_text_in_rows(self, text):
        table = self.browser.find_element(By.ID, "id_list_table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        self.assertIn(text, [row.text for row in rows])

    def test_start_to_do_list(self):
        self.browser.get(self.live_server_url)
        self.assertIn("To-Do", self.browser.title)

        header_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn("To-Do lists", header_text)

        input_box = self.browser.find_element(By.ID, "id_new_item")
        self.assertEqual(input_box.get_attribute("placeholder"), "Enter a to-do item")

        input_box.send_keys("Buy peacook feather")
        input_box.send_keys(Keys.ENTER)
        time.sleep(2)

        self.check_text_in_rows("1. Buy peacook feather")

        input_box = self.browser.find_element(By.ID, "id_new_item")
        input_box.send_keys("Make fly")
        input_box.send_keys(Keys.ENTER)

        time.sleep(2)

        self.check_text_in_rows("1. Buy peacook feather")
        self.check_text_in_rows("2. Make fly")
