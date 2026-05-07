from datetime import datetime


class SearchReport:

    def __init__(self, query, products, output_file="rapport_recherche.txt"):
        self.query = query
        self.products = products
        self.output_file = output_file
        self.lines = []

    def _build(self):
        self.lines = []
        add = self.lines.append

        add("=" * 60)
        add(f'RAPPORT DE RECHERCHE : "{self.query}"')
        add(f"Généré le : {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        add("=" * 60)

        add(f"\nNombre total de résultats trouvés : {len(self.products)}")

        add("\n3 Premiers Produits :")
        for i, product in enumerate(self.products[:3], start=1):
            add(f"  {i}. {product['name']}")
            add(f"     Prix : {product['price_text']}")

        priced = [p for p in self.products if p["price_value"] is not None]

        if priced:
            cheapest = min(priced, key=lambda p: p["price_value"])
            most_expensive = max(priced, key=lambda p: p["price_value"])

            add("\nProduit le moins cher :")
            add(f"  {cheapest['name']} — {cheapest['price_text']}")

            add("\nProduit le plus cher :")
            add(f"  {most_expensive['name']} — {most_expensive['price_text']}")
        else:
            add("\nAucun prix disponible pour le tri.")

        add("\nRECHERCHE RÉUSSIE!")

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
