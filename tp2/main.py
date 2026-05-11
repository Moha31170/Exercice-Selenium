from datetime import datetime

from selenium import webdriver

from pages.dynamic_controls_page import DynamicControlsPage
from pages.dynamic_loading_page import DynamicLoadingPage
from pages.notification_page import NotificationPage
from pages.infinite_scroll_page import InfiniteScrollPage


def log(message):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {message}")


def run_part(name, fn, page):
    print(f"\n--- {name} ---")
    try:
        fn()
        print(f"   RÉSULTAT : {name} RÉUSSI")
        return True
    except AssertionError as e:
        print(f"   [ECHEC] Assertion : {e}")
        page.take_screenshot(name.replace(" ", "_").lower())
        return False
    except Exception as e:
        print(f"   [ERREUR] {e}")
        page.take_screenshot(name.replace(" ", "_").lower())
        return False


def main():
    driver = webdriver.Chrome()
    results = {}

    print("\n" + "=" * 60)
    print("TP2 — TESTER DES CONTENUS DYNAMIQUES AVEC SELENIUM")
    print("=" * 60)

    try:
        page1 = DynamicControlsPage(driver)

        def scenario_dynamic_controls():
            log("Ouverture de la page Dynamic Controls")
            page1.open()

            log("Vérification de la présence de la checkbox")
            page1.verify_checkbox_present()
            print("   OK — Checkbox présente")

            log("Clic sur Remove")
            page1.click_remove()
            page1.wait_checkbox_removed()
            page1.verify_removed_message()
            print("   OK — Checkbox supprimée, message 'It's gone!' vérifié")

            log("Clic sur Add")
            page1.click_add()
            page1.wait_checkbox_added()
            page1.verify_added_message()
            print("   OK — Checkbox réapparue, message 'It's back!' vérifié")

            log("Vérification que le champ texte est désactivé")
            page1.verify_input_disabled()
            print("   OK — Champ texte désactivé")

            log("Clic sur Enable")
            page1.click_enable()
            page1.wait_input_enabled()
            page1.verify_input_enabled()
            print("   OK — Champ texte activé")

            log("Saisie dans le champ texte")
            page1.type_in_input("Test Selenium TP2")
            print("   OK — Texte saisi et vérifié")

        results["Partie 1 — Dynamic Controls"] = run_part(
            "Partie 1 — Dynamic Controls", scenario_dynamic_controls, page1
        )

        page2 = DynamicLoadingPage(driver)

        def scenario_dynamic_loading():
            log("Ouverture de la page Dynamic Loading — Exemple 2")
            page2.open_example_2()

            log("Vérification du bouton Start")
            page2.verify_start_button()
            print("   OK — Bouton Start présent")

            log("Clic sur Start")
            page2.click_start()

            log("Attente du contenu dynamique")
            page2.wait_for_content()
            page2.verify_hello_world()
            print("   OK — 'Hello World!' affiché")

        results["Partie 2 — Dynamic Loading"] = run_part(
            "Partie 2 — Dynamic Loading", scenario_dynamic_loading, page2
        )

        page3 = NotificationPage(driver)

        def scenario_notification():
            log("Ouverture de la page Notification Message")
            page3.open()

            for i in range(1, 4):
                log(f"Clic n°{i} sur 'Click here'")
                page3.click_here()
                page3.verify_notification_present()
                text = page3.verify_notification_is_expected()
                print(f"   OK — Message {i} : '{text}'")

        results["Partie 3 — Notification Message"] = run_part(
            "Partie 3 — Notification Message", scenario_notification, page3
        )

        page4 = InfiniteScrollPage(driver)

        def scenario_infinite_scroll():
            log("Ouverture de la page Infinite Scroll")
            page4.open()

            log("Vérification du contenu initial")
            page4.verify_initial_content()
            initial_count = page4.count_blocks()
            print(f"   OK — {initial_count} bloc(s) présent(s) au chargement")

            log("Scroll vers le bas (3 fois)")
            page4.scroll_down(times=3)

            log("Vérification du contenu supplémentaire")
            new_count = page4.verify_more_content(initial_count)
            print(f"   OK — Contenu augmenté : {initial_count} → {new_count} blocs")

        results["Partie 4 — Infinite Scroll"] = run_part(
            "Partie 4 — Infinite Scroll", scenario_infinite_scroll, page4
        )

    finally:
        print("\n" + "=" * 60)
        print("RÉCAPITULATIF")
        print("=" * 60)
        all_passed = True
        for part, passed in results.items():
            status = "RÉUSSI" if passed else "ÉCHOUÉ"
            print(f"  {part} : {status}")
            if not passed:
                all_passed = False

        print("-" * 60)
        print("RÉSULTAT GLOBAL :", "TP2 RÉUSSI" if all_passed else "TP2 ÉCHOUÉ")
        print("=" * 60)

        driver.quit()


if __name__ == "__main__":
    main()
