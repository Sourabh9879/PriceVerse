import os
from serpapi import GoogleSearch
from dotenv import load_dotenv

load_dotenv()

SERPAPI_KEY = os.getenv("SERPAPI_KEY")


def search_product(product_name):

    params = {
        "engine": "google_shopping",
        "q": product_name,
        "gl": "in",
        "hl": "en",
        "api_key": SERPAPI_KEY
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    products = []

    if "shopping_results" not in results:
        return []

    for item in results["shopping_results"]:

        products.append({

            "title": item.get("title"),

            "store": item.get("source"),

            "price": item.get("price"),

            "price_value": item.get("extracted_price", float("inf")),

            "thumbnail": item.get("thumbnail"),

            "link": item.get("product_link")

        })

    products.sort(key=lambda x: x["price_value"])

    return products[:5]