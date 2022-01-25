# Delivery-Fee-Calculator
An HTTP API (single endpoint) which calculates the delivery fee based on the information in the request payload (JSON) and includes the calculated delivery fee in the response payload (JSON).

Specification
Rules for calculating a delivery fee

- If the cart value is less than 10€, a small order surcharge is added to the delivery price. The surcharge is the difference between the cart value and 10€. For example if the cart value is 8.90€, the surcharge will be 1.10€.
- A delivery fee for the first 1000 meters (=1km) is 2€. If the delivery distance is longer than that, 1€ is added for every additional 500 meters that the courier needs to travel before reaching the destination. Even if the distance would be shorter than 500 meters, the minimum fee is always 1€.
- If the number of items is five or more, an additional 50 cent surcharge is added for each item above four
- The delivery fee can never be more than 15€, including possible surcharges.
- The delivery is free (0€) when the cart value is equal or more than 100€.
- During the Friday rush (3 - 7 PM UTC), the delivery fee (the total fee including possible surcharges) will be multiplied by 1.1x. However, the fee still cannot be more than the max (15€).

## Installation
To use this template, your computer needs:

- [Python 2 or 3](https://python.org)
- [Pip Package Manager](https://pypi.python.org/pypi)

## Running the app

    python3 app.py
    
## Client Request

    curl -i -H "Content-Type: application/json" -X POST -d '{"cart_value": 790, "delivery_distance": 2235, "number_of_items": 4, "time": "2021-10-12T13:00:00Z"}' http://localhost:5000/cart
    
### Example Json

    {"cart_value": 790, "delivery_distance": 2235, "number_of_items": 4, "time": "2021-10-12T13:00:00Z"}
    
## Fields

Field | Type | Description | Example | value
--- | --- | --- | --- | ---
cart_value | Integer | Value of the shopping cart in cents. | 790 (790 cents = 7.90€)
delivery_distance | Integer | The distance between the store and customer’s location in meters. | 2235 (2235 meters = 2.235 km)
number_of_items | Integer | The number of items in the customer's shopping cart. | 4 (customer has 4 items in the cart)
time | String | Order time in ISO format. | 2021-01-16T13:00:00Z
