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

    return jsonify({"message": "Customer Created", "results": customer_schema.dump(new_customer)}), 200

def get_customers(req):
    customers = db.session.query(Customer).all()

    if customers:
        return jsonify({"message" : "Customers Found", "results" : customers_schema.dump(customers)}), 200
    
    return jsonify({"message" : "Customers not found"}), 404

def get_customer_by_id(req, customer_id):
    customer = db.session.query(Customer).filter(Customer.customer_id == customer_id).first()

    if customer:
        return jsonify({"message" : "Customer Found", "results" : customer_schema.dump(customer)}),200
    
    return jsonify({"message" : "Customer not found"}),404

def update_customer(req, customer_id):
    customer = db.session.query(Customer).filter(Customer.customer_id == customer_id).first()
    data = request.form if request.form else request.get_json()

    populate_object(customer, data)

    if customer:
        try:
            db.session.commit()
            return jsonify({"message" : "Customer Updated", "results" : customer_schema.dump(customer)}),200
        except:
            db.session.rollback()
            return jsonify({"message" : "Not able to update customer"}),400

    return jsonify({"message" : "Customer not found"}),404

def delete_customer(req, customer_id):
    customer = db.session.query(Customer).filter(Customer.customer_id == customer_id).first()
    # data = request.form if request.form else request.get_json()

    if customer:
        try:
            db.session.delete(customer)
            db.session.commit()
            return jsonify({"message" : "Customer Deleted"}),200
        except:
            db.session.rollback()
            return jsonify({"message" : "Not able to delete customer"}),400

    return jsonify({"message" : "Customer not found"}),404