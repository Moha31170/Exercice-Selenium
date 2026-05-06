from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def exercice10():
    driver = webdriver.Chrome()

    wait = WebDriverWait(driver, 10)

    try:
        print("1. Navigation vers https://practicesoftwaretesting.com/...")
        driver.get("https://practicesoftwaretesting.com/")

        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".card")))
        print("   Produits chargés")

        cards = driver.find_elements(By.CSS_SELECTOR, ".card")
        assert len(cards) > 0, "Aucun produit trouvé sur la page"
        print(f"   {len(cards)} produits trouvés\n")

        products = []
        for card in cards:
            name_element = card.find_element(By.CSS_SELECTOR, ".card-title")
            name = name_element.text.strip()

            try:
                price_element = card.find_element(
                    By.CSS_SELECTOR, ".card-img-overlay .float-end"
                )
                price = price_element.text.strip()
            except Exception:
                price = "Prix non disponible"

            card_classes = card.get_attribute("class")
            out_of_stock = "out-of-stock" in card_classes

            products.append(
                {
                    "name": name,
                    "price": price,
                    "out_of_stock": out_of_stock,
                }
            )

        assert len(products) == len(
            cards
        ), f"Incohérence : {len(cards)} cartes mais {len(products)} produits extraits"

        print("=== 5 premiers produits ===")
        for product in products[:5]:
            stock_info = " [RUPTURE DE STOCK]" if product["out_of_stock"] else ""
            print(f"  - {product['name']} | {product['price']}{stock_info}")

        print(f"\n=== Liste complète ({len(products)} produits) ===")
        for index, product in enumerate(products, start=1):
            stock_info = " [RUPTURE DE STOCK]" if product["out_of_stock"] else ""
            print(f"  {index:2}. {product['name']} | {product['price']}{stock_info}")

    except AssertionError as e:
        print(f"Erreur d'assertion : {e}")

    except Exception as e:
        print(f"Erreur : {e}")

    finally:
        print("\n2. Fermeture du navigateur...")
        driver.quit()
        print("   Fermé")


if __name__ == "__main__":
    exercice10()
