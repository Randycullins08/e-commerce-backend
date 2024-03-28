from flask import request, Blueprint

import controllers

customer = Blueprint('customer', __name__)

@customer.route('/customer', methods=['POST'])
def add_customer():
    return controllers.add_customer(request)

@customer.route('/customer', methods=['GET'])
def get_customers():
    return controllers.get_customers(request)

@customer.route('/customer/<customer_id>', methods=['GET'])
def get_customer_by_id(customer_id):
    return controllers.get_customer_by_id(request, customer_id)