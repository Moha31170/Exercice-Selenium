from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def exercice9():
    driver = webdriver.Chrome()

    wait = WebDriverWait(driver, 10)

    try:
        print(
            "1. Navigation vers https://the-internet.herokuapp.com/dynamic_loading/1..."
        )
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

        driver.find_element(By.XPATH, "//button[text()='Start']").click()
        print("   Bouton 'Start' cliqué")

        finish_element = wait.until(EC.visibility_of_element_located((By.ID, "finish")))
        print("   Élément dynamique apparu")

        assert (
            "Hello World!" in finish_element.text
        ), f"Texte inattendu : {finish_element.text}"
        print(f"   Texte vérifié : {finish_element.text}")

        assert (
            "It's gone!" not in finish_element.text
        ), "Le texte contient 'It's gone!' alors qu'il ne devrait pas"
        print("   Vérification OK : 'It's gone!' absent du texte")

    except AssertionError as e:
        print(f"Erreur d'assertion : {e}")

    except Exception as e:
        print(f"Erreur : {e}")

    finally:
        print("2. Fermeture du navigateur...")
        driver.quit()
        print("   Fermé")


if __name__ == "__main__":
    exercice9()
