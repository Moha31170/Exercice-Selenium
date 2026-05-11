from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class NotificationPage(BasePage):
    URL = "https://the-internet.herokuapp.com/notification_message_rendered"

    CLICK_HERE_LINK = (By.LINK_TEXT, "Click here")
    NOTIFICATION = (By.CSS_SELECTOR, "#flash")

    EXPECTED_MESSAGES = [
        "Action successful",
        "Action unsuccesful, please try again",
    ]

    def open(self):
        self.driver.get(self.URL)
        self.wait_for_visible(self.CLICK_HERE_LINK)

    def get_notification_text(self):
        notification = self.wait_for_visible(self.NOTIFICATION)
        return notification.text.replace("×", "").strip()

    def click_here(self):
        self.wait_for_clickable(self.CLICK_HERE_LINK).click()

    def verify_notification_present(self):
        text = self.get_notification_text()
        assert text != "", "Aucun message de notification affiché"

    def verify_notification_is_expected(self):
        text = self.get_notification_text()
        assert any(
            expected in text for expected in self.EXPECTED_MESSAGES
        ), f"Message inattendu : '{text}'\nMessages attendus : {self.EXPECTED_MESSAGES}"
        return text
