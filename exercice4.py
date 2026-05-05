from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

try:
    print("1. Navigation vers https://the-internet.herokuapp.com/dropdown...")
    driver.get("https://the-internet.herokuapp.com/dropdown")

    dropdown_element = driver.find_element(By.ID, "dropdown")
    dropdown = Select(dropdown_element)

    dropdown.select_by_visible_text("Option 1")
    print("   'Option 1' sélectionné")

    selected = dropdown.first_selected_option
    assert selected.text == "Option 1", f"Texte sélectionné incorrect : {selected.text}"
    assert (
        selected.get_attribute("value") == "1"
    ), f"Valeur incorrecte : {selected.get_attribute('value')}"
    print(
        f"   Vérification OK : '{selected.text}' (value={selected.get_attribute('value')})"
    )

    dropdown.select_by_visible_text("Option 2")
    print("   'Option 2' sélectionné")

    selected = dropdown.first_selected_option
    assert selected.text == "Option 2", f"Texte sélectionné incorrect : {selected.text}"
    assert (
        selected.get_attribute("value") == "2"
    ), f"Valeur incorrecte : {selected.get_attribute('value')}"
    print(
        f"   Vérification OK : '{selected.text}' (value={selected.get_attribute('value')})"
    )

except AssertionError as e:
    print(f"Erreur d'assertion : {e}")

except Exception as e:
    print(f"Erreur : {e}")

finally:
    print("2. Fermeture du navigateur...")
    driver.quit()
    print("   Fermé")
