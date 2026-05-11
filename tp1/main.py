import os
from datetime import datetime

from selenium import webdriver

from pages.login_page import LoginPage
from pages.secure_area_page import SecureAreaPage
from pages.dropdown_page import DropdownPage
from pages.add_remove_page import AddRemovePage

# Identifiants
USERNAME = "tomsmith"
PASSWORD = "SuperSecretPassword!"


def take_screenshot(driver, step_name):
    os.makedirs("screenshots", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"screenshots/erreur_{step_name}_{timestamp}.png"
    driver.save_screenshot(filename)
    print(f"   [SCREENSHOT] Capture sauvegardée : {filename}")


def log(message):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {message}")


def main():
    driver = webdriver.Chrome()
    success = True

    print("\n" + "=" * 60)
    print("TP1 — CONTRÔLE D'ACCÈS ET VÉRIFICATIONS D'INTERFACE")
    print("=" * 60)

    try:

        print("\n--- Partie 1 : Authentification ---")

        login_page = LoginPage(driver)
        secure_page = SecureAreaPage(driver)

        log("Ouverture de la page de login")
        login_page.open()

        log("Vérification de la page de login")
        login_page.verify_page()
        print("   OK — Page de login confirmée")

        log(f"Connexion avec '{USERNAME}'")
        login_page.login(USERNAME, PASSWORD)

        log("Vérification du succès de la connexion")
        secure_page.verify_login_success()
        print("   OK — Connexion réussie, message de succès présent")

        log("Vérification du bouton logout")
        secure_page.verify_logout_button()
        print("   OK — Bouton logout visible")

        log("Déconnexion")
        secure_page.logout()

        log("Vérification de la redirection vers login")
        secure_page.verify_redirected_to_login()
        print("   OK — Retour sur la page de login confirmé")

        print("\n--- Partie 2 : Liste déroulante ---")

        dropdown_page = DropdownPage(driver)

        log("Ouverture de la page Dropdown")
        dropdown_page.open()

        log("Vérification de la présence du dropdown")
        dropdown_page.verify_dropdown_present()
        print("   OK — Liste déroulante présente")

        log("Sélection de 'Option 1'")
        dropdown_page.select_option("Option 1")
        dropdown_page.verify_selected("Option 1")
        print("   OK — Option 1 sélectionnée et vérifiée")

        log("Sélection de 'Option 2'")
        dropdown_page.select_option("Option 2")
        dropdown_page.verify_selected("Option 2")
        print("   OK — Option 2 sélectionnée et vérifiée")

        print("\n--- Partie 3 : Ajout et suppression d'éléments ---")

        add_remove_page = AddRemovePage(driver)

        log("Ouverture de la page Add/Remove Elements")
        add_remove_page.open()

        log("Ajout de 3 éléments")
        add_remove_page.add_elements(3)
        add_remove_page.verify_delete_count(3)
        print("   OK — 3 boutons Delete présents")

        log("Suppression d'un élément")
        add_remove_page.delete_one()
        add_remove_page.verify_delete_count(2)
        print("   OK — 2 boutons Delete restants")

        log("Suppression de tous les éléments restants")
        add_remove_page.delete_all()
        add_remove_page.verify_delete_count(0)
        print("   OK — Aucun bouton Delete restant")

    except AssertionError as e:
        success = False
        print(f"\n   [ECHEC] Assertion échouée : {e}")
        take_screenshot(driver, "assertion")

    except Exception as e:
        success = False
        print(f"\n   [ERREUR] {e}")
        take_screenshot(driver, "exception")

    finally:
        print("\n" + "=" * 60)
        if success:
            print("RÉSULTAT : TP1 RÉUSSI")
        else:
            print("RÉSULTAT : TP1 ÉCHOUÉ")
        print("=" * 60)
        driver.quit()


if __name__ == "__main__":
    main()
