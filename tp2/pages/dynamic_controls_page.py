from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class DynamicControlsPage(BasePage):
    URL = "https://the-internet.herokuapp.com/dynamic_controls"

    CHECKBOX = (By.CSS_SELECTOR, "input[type='checkbox']")
    REMOVE_ADD_BTN = (By.CSS_SELECTOR, "#checkbox-example button")
    CHECKBOX_MSG = (By.CSS_SELECTOR, "#checkbox-example #message")

    TEXT_INPUT = (By.CSS_SELECTOR, "#input-example input[type='text']")
    ENABLE_DISABLE_BTN = (By.CSS_SELECTOR, "#input-example button")
    INPUT_MSG = (By.CSS_SELECTOR, "#input-example #message")

    LOADING = (By.CSS_SELECTOR, "#checkbox-example #loading, #input-example #loading")

    def open(self):
        self.driver.get(self.URL)
        self.wait_for_visible((By.TAG_NAME, "h4"))

    def verify_checkbox_present(self):
        checkbox = self.wait_for_visible(self.CHECKBOX)
        assert checkbox.is_displayed(), "La case à cocher n'est pas visible"

    def click_remove(self):
        self.wait_for_clickable(self.REMOVE_ADD_BTN).click()

    def wait_checkbox_removed(self):
        self.wait_for_invisible(self.CHECKBOX)

    def verify_removed_message(self):
        msg = self.wait_for_visible(self.CHECKBOX_MSG)
        assert "It's gone!" in msg.text, f"Message inattendu après Remove : {msg.text}"

    def click_add(self):
        self.wait_for_clickable(self.REMOVE_ADD_BTN).click()

    def wait_checkbox_added(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.CHECKBOX)
        )

    def verify_added_message(self):
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(self.CHECKBOX_MSG, "It's back!")
        )
        msg = self.driver.find_element(*self.CHECKBOX_MSG)
        assert "It's back!" in msg.text

    def verify_input_disabled(self):
        input_field = self.wait_for_present(self.TEXT_INPUT)
        assert not input_field.is_enabled(), "Le champ devrait être désactivé au départ"

    def click_enable(self):
        self.wait_for_clickable(self.ENABLE_DISABLE_BTN).click()

    def wait_input_enabled(self):
        self.wait.until(EC.element_to_be_clickable(self.TEXT_INPUT))

    def verify_input_enabled(self):
        input_field = self.driver.find_element(*self.TEXT_INPUT)
        assert input_field.is_enabled(), "Le champ devrait être activé"

    def type_in_input(self, text):
        input_field = self.driver.find_element(*self.TEXT_INPUT)
        input_field.clear()
        input_field.send_keys(text)
        assert (
            input_field.get_attribute("value") == text
        ), f"Texte saisi incorrect : {input_field.get_attribute('value')}"
