"""Check the course data against both live backend API endpoints."""

import json
import os
from pathlib import Path
from urllib.parse import quote
from urllib.request import Request, urlopen

root = Path(__file__).resolve().parent
product_url = os.environ.get("PRODUCT_API_URL", "http://127.0.0.1:5100").rstrip("/")
pricing_url = os.environ.get("PRICING_API_URL", "http://127.0.0.1:5180").rstrip("/")
products = json.loads((root / "products_list/products.json").read_text())["products"]
dealers = json.loads((root / "dealer_details/utils/dealers.json").read_text())["dealers"]


def get(url):
    request = Request(url, headers={"Origin": "http://127.0.0.1:5101"})
    with urlopen(request, timeout=15) as response:
        assert response.status == 200
        assert response.headers.get("Access-Control-Allow-Origin") in ("*", "http://127.0.0.1:5101")
        return json.load(response)


assert get(product_url + "/products")["products"] == [item["product"] for item in products]
checked = 0
for product in products:
    name = product["product"]
    expected = {dealer["Dealer"]: dealer["products"][name] for dealer in dealers if name in dealer["products"]}
    supplied = get(product_url + "/getdealers/" + quote(name))["dealers"]
    assert set(supplied) == set(expected), f"Dealer names mismatch for {name}"
    for dealer in supplied:
        actual = get(pricing_url + "/price/" + quote(dealer) + "/" + quote(name))
        assert actual["message"] == f"{name} costs {expected[dealer]} at {dealer}"
        checked += 1
    all_prices = get(pricing_url + "/allprice/" + quote(name))["prices"]
    assert {item["key"]: item["value"] for item in all_prices} == expected
print(f"Passed: {len(products)} products, {checked} individual dealer prices, four complete price lists, and cross-origin API access.")
