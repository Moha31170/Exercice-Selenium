from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class SearchPage:
    URL = "https://practicesoftwaretesting.com"

    SEARCH_INPUT = (By.CSS_SELECTOR, "input[data-test='search-query']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[data-test='search-submit']")
    PRODUCT_CARDS = (By.CSS_SELECTOR, ".card")
    CARD_TITLE = (By.CSS_SELECTOR, "[data-test='product-name']")
    CARD_PRICE = (By.CSS_SELECTOR, "[data-test='product-price']")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self):
        self.driver.get(self.URL)

    def verify_search_form(self):
        search_input = self.wait.until(
            EC.visibility_of_element_located(self.SEARCH_INPUT)
        )
        assert search_input.is_displayed(), "Le champ de recherche n'est pas visible"

        search_button = self.wait.until(
            EC.visibility_of_element_located(self.SEARCH_BUTTON)
        )
        assert search_button.is_displayed(), "Le bouton de recherche n'est pas visible"

    def search(self, query):
        search_input = self.wait.until(
            EC.visibility_of_element_located(self.SEARCH_INPUT)
        )

        search_input.clear()
        search_input.send_keys(query)

        search_button = self.driver.find_element(*self.SEARCH_BUTTON)
        search_button.click()

        self.wait.until(EC.presence_of_all_elements_located(self.PRODUCT_CARDS))

        time.sleep(5)

    def verify_results_loaded(self):
        cards = self.driver.find_elements(*self.PRODUCT_CARDS)
        assert len(cards) > 0, "Aucun résultat affiché après la recherche"

    def get_results(self):
        cards = self.driver.find_elements(*self.PRODUCT_CARDS)
        products = []

        for card in cards:
            try:
                name = card.find_element(*self.CARD_TITLE).text.strip()
            except Exception:
                continue

            try:
                price_text = card.find_element(*self.CARD_PRICE).text.strip()
                price_value = float(
                    price_text.replace("$", "").replace("£", "").strip()
                )
            except Exception:
                price_text = "N/A"
                price_value = None

            products.append(
                {
                    "name": name,
                    "price_text": price_text,
                    "price_value": price_value,
                }
            )

        return products
