from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def exercice8():
    driver = webdriver.Chrome()

    wait = WebDriverWait(driver, 10)

    try:
        # 1. Accéder à la page des alertes JavaScript
        print(
            "1. Navigation vers https://the-internet.herokuapp.com/javascript_alerts..."
        )
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")

        driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
        print("   Bouton 'JS Alert' cliqué")

        alert = wait.until(EC.alert_is_present())

        print(f"   Message de l'alerte : {alert.text}")

        alert.accept()
        print("   Alerte acceptée")

        result = driver.find_element(By.ID, "result")
        assert (
            "You successfully clicked an alert" in result.text
        ), f"Message inattendu après acceptation : {result.text}"
        print(f"   Résultat vérifié : {result.text}")

        driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
        print("   Bouton 'JS Confirm' cliqué")

        alert = wait.until(EC.alert_is_present())
        print(f"   Message de la confirmation : {alert.text}")

        alert.dismiss()
        print("   Confirmation refusée")

        result = driver.find_element(By.ID, "result")
        assert (
            "You clicked: Cancel" in result.text
        ), f"Message inattendu après refus : {result.text}"
        print(f"   Résultat vérifié : {result.text}")

    except AssertionError as e:
        print(f"Erreur d'assertion : {e}")

    except Exception as e:
        print(f"Erreur : {e}")

    finally:
        print("2. Fermeture du navigateur...")
        driver.quit()
        print("   Fermé")


if __name__ == "__main__":
    exercice8()
