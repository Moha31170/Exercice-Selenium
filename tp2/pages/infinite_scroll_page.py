import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class InfiniteScrollPage(BasePage):
    URL = "https://the-internet.herokuapp.com/infinite_scroll"
    TEXT_BLOCKS = (By.CSS_SELECTOR, ".jscroll-added")

    def open(self):
        self.driver.get(self.URL)
        self.wait_for_visible(self.TEXT_BLOCKS)

    def count_blocks(self):
        return len(self.driver.find_elements(*self.TEXT_BLOCKS))

    def verify_initial_content(self):
        count = self.count_blocks()
        assert count > 0, "Aucun bloc de texte trouvé au chargement"

    def scroll_down(self, times=3, pause=1.5):
        for _ in range(times):
            self.scroll_to_bottom()
            time.sleep(pause)

    def verify_more_content(self, initial_count):
        new_count = self.count_blocks()
        assert new_count > initial_count, (
            f"Aucun contenu supplémentaire après scroll — "
            f"avant : {initial_count}, après : {new_count}"
        )
        return new_count
