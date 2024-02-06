from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from django.test import LiveServerTestCase
import time

MAX_TIME = 5


class NewVisitorTest(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.browser = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    def submit_item(self, text):
        input_box = self.browser.find_element(By.ID, "id_new_item")
        self.assertEqual(input_box.get_attribute("placeholder"), "Enter a to-do item")

        input_box.send_keys(text)
        input_box.send_keys(Keys.ENTER)

    def wait_text_in_rows(self, text):
        START_TIME = time.time()
        while True:
            try:
                table = self.browser.find_element(By.ID, "id_list_table")
                rows = table.find_elements(By.TAG_NAME, "tr")
                self.assertIn(text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - START_TIME > MAX_TIME:
                    raise e
                else:
                    time.sleep(0.2)

    def test_start_to_do_list(self):
        self.browser.get(self.live_server_url)
        self.assertIn("To-Do", self.browser.title)

        header_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn("To-Do lists", header_text)

        self.submit_item("Buy peacook feather")
        self.wait_text_in_rows("1. Buy peacook feather")

        self.submit_item("Make fly")
        self.wait_text_in_rows("1. Buy peacook feather")
        self.wait_text_in_rows("2. Make fly")
