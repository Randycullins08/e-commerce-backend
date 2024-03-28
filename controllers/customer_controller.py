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

def get_customers(req):
    customers = db.session.query(Customer).all()

    if customers:
        return jsonify({"message" : "Customers Found", "results" : customers_schema.dump(customers)}), 200
    else:
        return jsonify({"message" : "Customers not found"}), 404

def get_customer_by_id(req, customer_id):
    customer = db.session.query(Customer).filter(Customer.customer_id == customer_id).first()

    if customer:
        return jsonify({"message" : "Customer Found", "results" : customer_schema.dump(customer)}),200
    else: 
        return jsonify({"message" : "Customer not found"}),404