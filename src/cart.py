from flask import request, jsonify
from flask_restful import Resource
import math
from datetime import datetime, time
from utils import is_time_between

class Cart(Resource):
    def __init__(self):
        self.cart_value = request.json["cart_value"]
        self.delivery_distance = request.json["delivery_distance"]
        self.number_of_items = request.json["number_of_items"]
        self.delivery_fee = 0

    def small_price_fee(self):
        '''
        If the cart value is less than 10€, a small order surcharge is added to the delivery price.
        '''
        if self.cart_value < 1000:
            self.delivery_fee = 1000 - self.cart_value

    def check_fee_threshold(self):
        '''
        The delivery fee can never be more than 15€, including possible surcharges.
        '''
        if self.delivery_fee > 1500:
            self.delivery_fee = 1500

    def rush_charge(self):
        ''''
        During the Friday rush (3 - 7 PM UTC), the delivery fee (the total fee including possible surcharges) will be multiplied by 1.1x. H
        owever, the fee still cannot be more than the max (15€).
        '''
        if datetime.today().weekday() == 4:
            if is_time_between(time(15, 00), time(19, 00)):
                self.delivery_fee *= 1.1
                self.check_fee_threshold()

    def delivery_fee_calculator(self):
        '''
        A delivery fee for the distance
        '''
        if self.delivery_distance <= 1000:
            self.delivery_fee += 200
        else:
            self.delivery_fee += 200 + (math.ceil(self.delivery_distance  / 500) - 2) * 100 

    def quantity_fee(self):
        '''
        If the number of items is five or more, an additional 50 cent surcharge is added for each item above four
        '''
        if self.number_of_items == 5:
            self.cart_value += 500
        elif self.number_of_items > 5:
            self.cart_value += (self.number_of_items - 5) * 500

    def zero_delivery_fee(self):
        '''
        The delivery is free (0€) when the cart value is equal or more than 100€.
        '''
        if self.cart_value >= 10000:
            self.delivery_fee = 0

    def post(self):
        self.small_price_fee()
        self.delivery_fee_calculator()
        self.quantity_fee()
        self.check_fee_threshold()
        self.zero_delivery_fee()
        self.rush_charge()

        return jsonify({"delivery_fee": self.delivery_fee})