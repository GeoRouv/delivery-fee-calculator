from flask import Flask
from flask_restful import Api
from cart import Cart

app = Flask(__name__)
api = Api(app)

'''
Make this kind of request from client-side:

$ curl -i -H "Content-Type: application/json" -X POST -d '{"cart_value": 790, "delivery_distance": 2235, "number_of_items": 4, "time": "2021-10-12T13:00:00Z"}' http://localhost:5000/cart

or

Use Postman! 

'''


api.add_resource(Cart, '/cart')

if __name__ == '__main__':

    try:
        app.run()
    except:
        print('Unable to open port')
