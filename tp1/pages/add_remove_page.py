from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddRemovePage:
    URL = "https://the-internet.herokuapp.com/add_remove_elements/"

    ADD_BUTTON = (By.CSS_SELECTOR, "button[onclick='addElement()']")
    DELETE_BUTTON = (By.CSS_SELECTOR, "button.added-manually")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self):
        self.driver.get(self.URL)
        self.wait.until(EC.visibility_of_element_located(self.ADD_BUTTON))

    def add_elements(self, count):
        button = self.wait.until(EC.element_to_be_clickable(self.ADD_BUTTON))
        for _ in range(count):
            self.driver.execute_script("arguments[0].click();", button)

    def get_delete_buttons(self):
        return self.driver.find_elements(*self.DELETE_BUTTON)

    def verify_delete_count(self, expected_count):
        try:
            self.wait.until(lambda d: len(self.get_delete_buttons()) == expected_count)
        except Exception:
            pass

        buttons = self.get_delete_buttons()
        assert (
            len(buttons) == expected_count
        ), f"Nombre de boutons Delete incorrect — attendu : {expected_count}, obtenu : {len(buttons)}"

    def delete_one(self):
        buttons = self.get_delete_buttons()
        assert len(buttons) > 0, "Aucun bouton Delete disponible"
        self.driver.execute_script("arguments[0].click();", buttons[0])

    def delete_all(self):
        while True:
            buttons = self.get_delete_buttons()
            if not buttons:
                break
            self.driver.execute_script("arguments[0].click();", buttons[0])
