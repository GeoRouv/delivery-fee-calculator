# Delivery-Fee-Calculator
A simple flask app for calculating delivery fees

## Installation
To use this template, your computer needs:

- [Python 2 or 3] (https://python.org)
- [Pip Package Manager](https://pypi.python.org/pypi)

## Running the app

    python3 app.py
    
## Client Request

    curl -i -H "Content-Type: application/json" -X POST -d '{"cart_value": 790, "delivery_distance": 2235, "number_of_items": 4, "time": "2021-10-12T13:00:00Z"}' http://localhost:5000/cart
