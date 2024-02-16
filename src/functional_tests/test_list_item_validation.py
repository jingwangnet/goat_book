from .base import FunctionalTest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class ItemValidationTest(FunctionalTest):
    def test_cannote_add_empty_list_items(self):
        self.browser.get(self.live_server_url)
        self.submit_item("")

        self.wait_for(
            lambda: self.assertEqual(
                self.browser.find_element(By.CSS_SELECTOR, ".invalid-feedback").text,
                "You can't have an empty list item",
            )
        )

        self.submit_item("Buy milk")
        self.wait_text_in_rows("1. Buy milk")

        self.submit_item("")
        self.wait_for(
            lambda: self.assertEqual(
                self.browser.find_element(By.CSS_SELECTOR, ".invalid-feedback").text,
                "You can't have an empty list item",
            )
        )

        self.submit_item("Make tea")
        self.wait_text_in_rows("2. Make tea")
        self.wait_text_in_rows("1. Buy milk")
