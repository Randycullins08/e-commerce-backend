from flask import jsonify, request
from db import db

from models.customer import Customer, customer_schema, customers_schema
from util.reflection import populate_object

def add_customer(req):
    data = request.form if request.form else request.get_json()

    new_customer = Customer.new_customer_obj()
    populate_object(new_customer, data)

    try:
        db.session.add(new_customer)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "Unable to create customer"}), 400

    return jsonify({"message": "product created", "results": customer_schema.dump(new_customer)}), 200