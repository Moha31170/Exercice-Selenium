from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    print("1. Navigation vers https://example.com...")
    driver.get("https://example.com")

    link = driver.find_element(By.TAG_NAME, "a")
    print(f"   Élément trouvé : {link.text}")

    assert (
        link.tag_name == "a"
    ), f"L'élément n'est pas un lien, tag trouvé : {link.tag_name}"
    print(f"   Type d'élément vérifié : <{link.tag_name}>")

    href = link.get_attribute("href")
    assert href and href.strip() != "", "L'attribut href est vide ou absent"
    print(f"   Attribut href vérifié : non vide")

    print(f"   URL du lien : {href}")

except AssertionError as e:
    print(f"Erreur d'assertion : {e}")

except Exception as e:
    print(f"Erreur : {e}")

finally:
    print("2. Fermeture du navigateur...")
    driver.quit()
    print("   Fermé")
