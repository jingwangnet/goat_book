from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest


class LayoutAndStylingTest(FunctionalTest):
    def test_layout_and_styling(self):
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        input_box = self.browser.find_element(By.ID, "id_new_item")
        self.assertAlmostEqual(
            input_box.location["x"] + input_box.size["width"] / 2, 512, delta=30
        )

        self.submit_item("Buy peacook feather")

        input_box = self.browser.find_element(By.ID, "id_new_item")
        self.assertAlmostEqual(
            input_box.location["x"] + input_box.size["width"] / 2, 512, delta=30
        )


