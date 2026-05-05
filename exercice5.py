from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    print("1. Navigation vers https://the-internet.herokuapp.com/checkboxes...")
    driver.get("https://the-internet.herokuapp.com/checkboxes")

    checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
    assert len(checkboxes) == 2, f"Nombre de checkboxes inattendu : {len(checkboxes)}"
    print(f"   {len(checkboxes)} checkboxes trouvées")

    checkbox_1 = checkboxes[0]
    checkbox_2 = checkboxes[1]

    print(
        f"   État initial — case 1 : {'cochée' if checkbox_1.is_selected() else 'décochée'}"
    )
    print(
        f"   État initial — case 2 : {'cochée' if checkbox_2.is_selected() else 'décochée'}"
    )

    if not checkbox_1.is_selected():
        checkbox_1.click()
        print("   Case 1 cochée")

    assert checkbox_1.is_selected(), "La checkbox 1 devrait être cochée"
    print("   Vérification OK : case 1 est cochée")

    if checkbox_2.is_selected():
        checkbox_2.click()
        print("   Case 2 décochée")

    assert not checkbox_2.is_selected(), "La checkbox 2 devrait être décochée"
    print("   Vérification OK : case 2 est décochée")

except AssertionError as e:
    print(f"Erreur d'assertion : {e}")

except Exception as e:
    print(f"Erreur : {e}")

finally:
    print("2. Fermeture du navigateur...")
    driver.quit()
    print("   Fermé")
