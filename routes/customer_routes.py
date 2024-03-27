from flask import request, Blueprint

from controllers import customer_controller

customer = Blueprint('customer', __name__)

@customer.route('/customer', methods=['POST'])
def add_customer():
    return customer_controller.add_customer(request)