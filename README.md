# Dealer Evaluation Backends

Course starter: https://github.com/ibm-developer-skills-network/dealer_evaluation_backend

This repository contains the Python Product Details service and Node.js Dealer
Pricing service for the course final project.

## Current status

Both services pass the local integration check: four products, twelve individual
dealer prices, four complete price lists, and cross-origin access. The Laptop
dealer spelling is consistent between services. Dockerfiles use Python 3.13 and
Node.js 22.

Code Engine deployment is pending course-provided access. The personal IBM Cloud
trial account rejected project creation because it requires a paid account.
No Code Engine deployment or URL is claimed here.

## Local run

Install `products_list/requirements.txt` into a Python environment, then start
the product service from `products_list/`:

```text
python -m flask --app app run --host=127.0.0.1 --port=5100 --no-reload
```

From `dealer_details/`, run `npm ci`. Set `PORT=5180` and run `npm start`.
Run `python verify_api.py` from this repository to check both APIs.

Code Engine container ports are 5000 for Product Details and 8080 for Dealer Pricing.
