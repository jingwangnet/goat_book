from .base import FunctionalTest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(FunctionalTest):
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

    def test_create_multiple_lists_on_difference_urls(self):
        self.browser.get(self.live_server_url)
        self.submit_item("Buy peacook feather")
        self.wait_text_in_rows("1. Buy peacook feather")

        JIMMY_URL = self.browser.current_url
        self.assertRegex(JIMMY_URL, "/lists/.+")

        self.browser.delete_all_cookies()
        self.browser.get(self.live_server_url)

        page = self.browser.find_element(By.TAG_NAME, "body").text
        self.assertNotIn("Buy peacook feather", page)

        self.submit_item("Buy milk")
        self.wait_text_in_rows("1. Buy milk")

        JOHN_URL = self.browser.current_url
        self.assertRegex(JOHN_URL, "/lists/.+")
        self.assertNotEqual(JIMMY_URL, JOHN_URL)

        page = self.browser.find_element(By.TAG_NAME, "body").text
        self.assertNotIn("Buy peacook feather", page)
        self.assertIn("Buy milk", page)
