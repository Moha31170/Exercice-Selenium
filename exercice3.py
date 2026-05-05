from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    print("1. Navigation vers https://demoqa.com/text-box...")
    driver.get("https://demoqa.com/text-box")

    driver.find_element(By.ID, "userName").send_keys("John Doe")
    print("   Champ 'Full Name' rempli")

    driver.find_element(By.ID, "userEmail").send_keys("john@example.com")
    print("   Champ 'Email' rempli")

    driver.find_element(By.ID, "currentAddress").send_keys("123 Main Street")
    print("   Champ 'Current Address' rempli")

    submit_button = driver.find_element(By.ID, "submit")

    driver.execute_script("arguments[0].scrollIntoView();", submit_button)
    submit_button.click()
    print("   Bouton 'Submit' cliqué")

    output = wait.until(EC.visibility_of_element_located((By.ID, "output")))
    output_text = output.text

    assert "John Doe" in output_text, f"Nom non trouvé dans le résultat : {output_text}"
    assert (
        "john@example.com" in output_text
    ), f"Email non trouvé dans le résultat : {output_text}"
    assert (
        "123 Main Street" in output_text
    ), f"Adresse non trouvée dans le résultat : {output_text}"
    print(f"   Résultat vérifié :\n{output_text}")

except AssertionError as e:
    print(f"Erreur d'assertion : {e}")

except Exception as e:
    print(f"Erreur : {e}")

finally:
    print("2. Fermeture du navigateur...")
    driver.quit()
    print("   Fermé")
