from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BooksPage:
    URL = "https://books.toscrape.com"

    BOOK_CARDS = (By.CSS_SELECTOR, "article.product_pod")
    BOOK_TITLE = (By.CSS_SELECTOR, "h3 > a")
    BOOK_PRICE = (By.CSS_SELECTOR, ".price_color")
    BOOK_RATING = (By.CSS_SELECTOR, ".star-rating")
    BOOK_AVAILABILITY = (By.CSS_SELECTOR, ".availability")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self):
        self.driver.get(self.URL)
        self.wait.until(EC.presence_of_all_elements_located(self.BOOK_CARDS))

    def get_books(self):
        total = len(self.driver.find_elements(*self.BOOK_CARDS))
        books = []

        for index in range(total):
            cards = self.driver.find_elements(*self.BOOK_CARDS)
            card = cards[index]

            title_element = card.find_element(*self.BOOK_TITLE)
            title = title_element.get_attribute("title")

            price_text = card.find_element(*self.BOOK_PRICE).text.strip()
            price_value = float(price_text.replace("£", "").replace("Â", ""))

            rating_classes = card.find_element(*self.BOOK_RATING).get_attribute("class")
            rating = rating_classes.replace("star-rating", "").strip()

            availability = card.find_element(*self.BOOK_AVAILABILITY).text.strip()

            books.append(
                {
                    "title": title,
                    "price_text": price_text,
                    "price_value": price_value,
                    "rating": rating,
                    "availability": availability,
                }
            )

        return books
