import json
from collections import Counter
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
JSON_FILE = BASE_DIR / "data" / "kbeauty_favorites.json"


def load_data(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def show_summary(data):
    products = data["products"]

    brands = {
        product["brand"]
        for product in products
    }

    print("\nMY K-BEAUTY SHELF")
    print("-" * 50)

    print(f"Collection: {data['collection_name']}")
    print(f"Total products: {len(products)}")
    print(f"Total brands: {len(brands)}")


def show_products(products):
    print("\nALL PRODUCTS")
    print("-" * 50)

    for product in products:
        print(
            f"{product['brand']} | "
            f"{product['product_name']}"
        )


def show_products_by_brand(products):
    brand_counter = Counter(
        product["brand"]
        for product in products
    )

    print("\nPRODUCTS BY BRAND")
    print("-" * 50)

    for brand, total in brand_counter.most_common():
        print(f"{brand}: {total}")


def show_skincare_products(products):
    skincare_products = [
        product
        for product in products
        if product["category"] == "skincare"
    ]

    print("\nSKINCARE PRODUCTS")
    print("-" * 50)

    for product in skincare_products:
        print(
            f"{product['brand']} | "
            f"{product['product_name']}"
        )


def show_pdrn_products(products):
    pdrn_products = []

    for product in products:
        terms = [
            term.lower()
            for term in product["key_terms"]
        ]

        if "pdrn" in terms:
            pdrn_products.append(product)

    print("\nPDRN PRODUCTS")
    print("-" * 50)

    for product in pdrn_products:
        print(
            f"{product['brand']} | "
            f"{product['product_name']}"
        )


def main():
    data = load_data(JSON_FILE)

    products = data["products"]

    show_summary(data)
    show_products(products)
    show_products_by_brand(products)
    show_skincare_products(products)
    show_pdrn_products(products)


if __name__ == "__main__":
    main()