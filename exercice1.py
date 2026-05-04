from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    print("1. Navigation vers https://example.com...")
    driver.get("https://example.com")

    assert driver.title == "Example Domain", f"Titre incorrect : {driver.title}"
    print(f"   Titre vérifié : {driver.title}")

    body = driver.find_element(By.TAG_NAME, "body")
    assert (
        "Example Domain" in body.text
    ), "Le contenu 'Example Domain' est introuvable dans la page"
    print(f"   Contenu vérifié : 'Example Domain' trouvé dans la page")

except AssertionError as e:
    print(f"Erreur d'assertion : {e}")

except Exception as e:
    print(f"Erreur : {e}")

finally:
    print("2. Fermeture du navigateur...")
    driver.quit()
    print("   Fermé")
