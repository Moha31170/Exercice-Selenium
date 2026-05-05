from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def exercice6():
    driver = webdriver.Chrome()

    wait = WebDriverWait(driver, 10)

    try:
        print("1. Navigation vers https://practicesoftwaretesting.com/...")
        driver.get("https://practicesoftwaretesting.com/")

        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".card")))
        print("   Produits chargés")

        cards = driver.find_elements(By.CSS_SELECTOR, ".card")
        print(f"   Cartes produit trouvées : {len(cards)}")

        titles = driver.find_elements(By.CSS_SELECTOR, ".card-title")
        print(f"   Titres trouvés : {len(titles)}")

        assert len(titles) == len(
            cards
        ), f"Incohérence : {len(cards)} cartes mais {len(titles)} titres"

        invisible_cards = [card for card in cards if not card.is_displayed()]
        assert (
            len(invisible_cards) == 0
        ), f"{len(invisible_cards)} carte(s) non visible(s)"
        print("   Toutes les cartes sont visibles")

        invisible_titles = [title for title in titles if not title.is_displayed()]
        assert (
            len(invisible_titles) == 0
        ), f"{len(invisible_titles)} titre(s) non visible(s)"
        print("   Tous les titres sont visibles")

        print(f"   Nombre total de cartes produit : {len(cards)}")

    except AssertionError as e:
        print(f"Erreur d'assertion : {e}")

    except Exception as e:
        print(f"Erreur : {e}")

    finally:
        print("2. Fermeture du navigateur...")
        driver.quit()
        print("   Fermé")


if __name__ == "__main__":
    exercice6()
