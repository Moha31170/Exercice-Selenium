from selenium import webdriver
from SearchPage import SearchPage
from SearchReport import SearchReport

QUERY = "hammer"


def main():
    driver = webdriver.Chrome()

    try:
        page = SearchPage(driver)

        print("\n--- Phase 1: Navigation et Localisation ---")
        page.open()
        page.verify_search_form()
        print("Formulaire de recherche vérifié (champ + bouton visibles)")

        print(f'\n--- Phase 2: Recherche de "{QUERY}" ---')
        page.search(QUERY)
        page.verify_results_loaded()
        print("Résultats chargés")

        print("\n--- Phase 3: Extraction des Données ---")
        products = page.get_results()
        assert len(products) > 0, "Aucun produit extrait"
        print(f"{len(products)} produits extraits")

        report = SearchReport(QUERY, products, output_file="rapport_recherche.txt")
        report.generate()

    except AssertionError as e:
        print(f"Erreur d'assertion : {e}")

    except Exception as e:
        print(f"Erreur : {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
