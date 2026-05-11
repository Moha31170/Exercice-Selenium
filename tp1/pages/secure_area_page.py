from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SecureAreaPage:
    SUCCESS_FLASH = (By.CSS_SELECTOR, "#flash.success")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "a[href='/logout']")
    PAGE_HEADING = (By.TAG_NAME, "h2")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def verify_login_success(self):
        heading = self.wait.until(EC.visibility_of_element_located(self.PAGE_HEADING))
        assert (
            "Secure Area" in heading.text
        ), f"Page inattendue après login : {heading.text}"

        flash = self.driver.find_element(*self.SUCCESS_FLASH)
        assert (
            "You logged into a secure area!" in flash.text
        ), f"Message de succès absent : {flash.text}"

    def verify_logout_button(self):
        logout = self.wait.until(EC.visibility_of_element_located(self.LOGOUT_BUTTON))
        assert logout.is_displayed(), "Le bouton logout n'est pas visible"

    def logout(self):
        self.driver.find_element(*self.LOGOUT_BUTTON).click()

    def verify_redirected_to_login(self):
        self.wait.until(EC.url_contains("/login"))
        assert (
            "/login" in self.driver.current_url
        ), f"Redirection incorrecte : {self.driver.current_url}"
