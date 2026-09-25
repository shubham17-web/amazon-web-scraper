import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from datetime import date


HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def scrape_products():

    base_url = "https://books.toscrape.com/"

    products_data = []

    for page in range(1, 51):

        if page == 1:
            url = base_url
        else:
            url = f"{base_url}catalogue/page-{page}.html"

        try:
            response = requests.get(
                url,
                headers=HEADERS,
                timeout=30
            )

            response.raise_for_status()

        except requests.exceptions.RequestException as e:

            print(f"Page {page} failed:", e)
            continue

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        products = soup.find_all(
            "article",
            class_="product_pod"
        )

        print(
            f"Page {page}: {len(products)} products"
        )

        for product in products:

            title = product.find(
                "h3"
            ).find("a")["title"]

            price = product.find(
                "p",
                class_="price_color"
            ).get_text(strip=True)

            availability = product.find(
                "p",
                class_="instock"
            ).get_text(strip=True)

            rating = product.find(
                "p",
                class_="star-rating"
            )["class"][1]

            relative_url = product.find(
                "h3"
            ).find("a")["href"]

            product_url = urljoin(
                url,
                relative_url
            )

            data = {
                "title": title,
                "price": price,
                "availability": availability,
                "rating": rating,
                "product_url": product_url,
                "scraped_date": date.today()
            }

            products_data.append(data)

    return products_data