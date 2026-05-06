from collections import Counter

from selenium import webdriver
from BooksPage import BooksPage


def main():
    driver = webdriver.Chrome()

    print("\n" + "=" * 60)
    print("TP : EXTRACTION DE DONNÉES DE LIVRES")
    print("=" * 60)

    try:
        page = BooksPage(driver)

        print("\n--- Phase 1: Navigation ---")
        page.open()
        print("Accédé à books.toscrape.com")
        print("Livres chargés")

        print("\n--- Phase 2: Extraction des Données ---")
        books = page.get_books()

        assert len(books) > 0, "Aucun livre extrait"
        print(f"{len(books)} livres extraits avec succès")

        for i, book in enumerate(books, start=1):
            short_title = (
                book["title"][:20] + " ..."
                if len(book["title"]) > 20
                else book["title"]
            )
            print(f"Livre {i}: {short_title} - {book['price_text']} ({book['rating']})")

        print("\n--- Phase 3: Rapport et Statistiques ---")

        print(f"\nNombre total de livres: {len(books)}")

        print(f"\n5 Premiers Livres:")
        for book in books[:5]:
            print(f"  {books.index(book) + 1}. {book['title']}")
            print(
                f"     Prix: {book['price_text']} | Rating: {book['rating']} | {book['availability']}"
            )

        prices = [book["price_value"] for book in books]
        print(f"\nStatistiques de Prix:")
        print(f"  Prix moyen: £{sum(prices) / len(prices):.2f}")
        print(f"  Prix minimum: £{min(prices):.2f}")
        print(f"  Prix maximum: £{max(prices):.2f}")

        rating_counts = Counter(book["rating"] for book in books)
        print(f"\nDistribution par Note:")
        for rating, count in sorted(rating_counts.items()):
            print(f"  {rating} étoiles: {count} livres")

    except AssertionError as e:
        print(f"Erreur d'assertion : {e}")

    except Exception as e:
        print(f"Erreur : {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
