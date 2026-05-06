from collections import Counter
from datetime import datetime


class BooksReport:
    # test
    def __init__(self, books, output_file="rapport_livres.txt"):
        self.books = books
        self.output_file = output_file
        self.lines = []

    def _build(self):
        self.lines = []
        add = self.lines.append

        add("=" * 60)
        add("TP : EXTRACTION DE DONNÉES DE LIVRES")
        add(f"Généré le : {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        add("=" * 60)

        add("\n--- Phase 2: Extraction des Données ---")
        add(f"{len(self.books)} livres extraits avec succès")

        for i, book in enumerate(self.books, start=1):
            short_title = book["title"][:20] + " ..." if len(book["title"]) > 20 else book["title"]
            add(f"Livre {i}: {short_title} - {book['price_text']} ({book['rating']})")

        add("\n--- Phase 3: Rapport et Statistiques ---")
        add(f"\nNombre total de livres: {len(self.books)}")

        add("\n5 Premiers Livres:")
        for i, book in enumerate(self.books[:5], start=1):
            add(f"  {i}. {book['title']}")
            add(f"     Prix: {book['price_text']} | Rating: {book['rating']} | {book['availability']}")

        prices = [book["price_value"] for book in self.books]
        add("\nStatistiques de Prix:")
        add(f"  Prix moyen: £{sum(prices) / len(prices):.2f}")
        add(f"  Prix minimum: £{min(prices):.2f}")
        add(f"  Prix maximum: £{max(prices):.2f}")

        rating_counts = Counter(book["rating"] for book in self.books)
        add("\nDistribution par Note:")
        for rating, count in sorted(rating_counts.items()):
            add(f"  {rating} étoiles: {count} livres")

    def print_to_console(self):
        if not self.lines:
            self._build()
        print("\n" + "\n".join(self.lines))

    def save_to_file(self):
        if not self.lines:
            self._build()
        with open(self.output_file, "w", encoding="utf-8") as f:
            f.write("\n".join(self.lines))
        print(f"\nRapport enregistré dans : {self.output_file}")

    def generate(self):
        self._build()
        self.print_to_console()
        self.save_to_file()