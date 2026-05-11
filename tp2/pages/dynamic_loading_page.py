from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class DynamicLoadingPage(BasePage):
    URL_EXAMPLE_2 = "https://the-internet.herokuapp.com/dynamic_loading/2"

    START_BUTTON = (By.XPATH, "//button[text()='Start']")
    LOADING = (By.ID, "loading")
    FINISH_TEXT = (By.CSS_SELECTOR, "#finish h4")

    def open_example_2(self):
        self.driver.get(self.URL_EXAMPLE_2)
        self.wait_for_visible(self.START_BUTTON)

    def verify_start_button(self):
        btn = self.driver.find_element(*self.START_BUTTON)
        assert btn.is_displayed(), "Le bouton Start n'est pas visible"

    def click_start(self):
        self.wait_for_clickable(self.START_BUTTON).click()

    def wait_for_content(self):
        self.wait_for_invisible(self.LOADING)
        return self.wait_for_visible(self.FINISH_TEXT)

    def verify_hello_world(self):
        element = self.driver.find_element(*self.FINISH_TEXT)
        assert (
            "Hello World!" in element.text
        ), f"Texte inattendu après chargement : {element.text}"
