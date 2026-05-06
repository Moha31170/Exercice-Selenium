from selenium import webdriver
from BooksPage import BooksPage
from BooksReport import BooksReport


def main():
    driver = webdriver.Chrome()

    try:
        page = BooksPage(driver)

        print("\n--- Phase 1: Navigation ---")
        page.open()
        print("Accédé à books.toscrape.com")
        print("Livres chargés")

        print("\n--- Phase 2: Extraction des Données ---")
        books = page.get_books()
        assert len(books) > 0, "Aucun livre extrait"

        report = BooksReport(books, output_file="rapport_livres.txt")
        report.generate()

    except AssertionError as e:
        print(f"Erreur d'assertion : {e}")

    except Exception as e:
        print(f"Erreur : {e}")

    finally:
        #TEST
        driver.quit()


if __name__ == "__main__":
    main()