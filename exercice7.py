from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def exercice7():
    driver = webdriver.Chrome()

    wait = WebDriverWait(driver, 10)

    try:
        print("1. Navigation vers https://practicesoftwaretesting.com/...")
        driver.get("https://practicesoftwaretesting.com/")

        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".card")))
        print("   Produits chargés")

        cards = driver.find_elements(By.XPATH, "//*[contains(@class, 'card')]")
        assert len(cards) > 0, "Aucune carte trouvée avec XPath contains()"
        print(f"   Cartes trouvées avec contains(@class, 'card') : {len(cards)}")

        titles = driver.find_elements(By.XPATH, "//*[contains(@class, 'card-title')]")
        assert len(titles) > 0, "Aucun titre trouvé avec XPath"
        print(f"   Titres trouvés : {len(titles)}")

        first_two = driver.find_elements(
            By.XPATH, "//*[contains(@class, 'card')][position() <= 2]"
        )
        assert (
            len(first_two) == 2
        ), f"Nombre de cartes (position) inattendu : {len(first_two)}"
        print(f"   2 premières cartes via position() : {len(first_two)}")

        cards_without_row = driver.find_elements(
            By.XPATH, "//*[contains(@class, 'card') and not(contains(@class, 'row'))]"
        )
        assert len(cards_without_row) > 0, "Aucune carte sans 'row' trouvée"
        print(f"   Cartes sans classe 'row' via not() : {len(cards_without_row)}")

        cards_with_title = driver.find_elements(
            By.XPATH,
            "//*[contains(@class, 'card') and descendant::*[contains(@class, 'card-title')]]",
        )
        assert (
            len(cards_with_title) > 0
        ), "Aucune carte avec titre trouvée via descendant"
        print(f"   Cartes avec titre via descendant::* : {len(cards_with_title)}")

        print("   Tous les XPath fonctionnent correctement")

    except AssertionError as e:
        print(f"Erreur d'assertion : {e}")

    except Exception as e:
        print(f"Erreur : {e}")

    finally:
        print("2. Fermeture du navigateur...")
        driver.quit()
        print("   Fermé")


if __name__ == "__main__":
    exercice7()
