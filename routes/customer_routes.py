from flask import request, Blueprint

import controllers

customer = Blueprint('customer', __name__)

@customer.route('/customer', methods=['POST'])
def add_customer():
    return controllers.add_customer(request)