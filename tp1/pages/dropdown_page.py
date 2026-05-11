from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


class DropdownPage:
    URL = "https://the-internet.herokuapp.com/dropdown"
    DROPDOWN = (By.ID, "dropdown")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self):
        self.driver.get(self.URL)

    def verify_dropdown_present(self):
        element = self.wait.until(EC.visibility_of_element_located(self.DROPDOWN))
        assert element.is_displayed(), "La liste déroulante n'est pas visible"

    def select_option(self, text):
        element = self.wait.until(EC.visibility_of_element_located(self.DROPDOWN))
        Select(element).select_by_visible_text(text)

    def get_selected_option(self):
        element = self.wait.until(EC.visibility_of_element_located(self.DROPDOWN))
        return Select(element).first_selected_option.text

    def verify_selected(self, expected_text):
        selected = self.get_selected_option()
        assert (
            selected == expected_text
        ), f"Option sélectionnée incorrecte — attendu : '{expected_text}', obtenu : '{selected}'"
