from flask import Flask, jsonify, request
import psycopg2
from flask_marshmallow import Marshmallow
import os

from routes.__init__ import *

from db import *
from util.reflection import populate_object
from models.customer import Customer, customer_schema, customers_schema
from models.order import Order, order_schema, orders_schema
from models.product import Product, product_schema, products_schema
from models.product_category import ProductCategory, product_category_schema, product_categories_schema

flask_host = os.environ.get("FLASK_HOST")
flask_port = os.environ.get("FLASK_POST")

database_scheme = os.environ.get("DATABASE_SCHEME")
database_user = os.environ.get("DATABASE_USER")
database_address = os.environ.get("DATABASE_ADDRESS")
database_port = os.environ.get("DATABASE_PORT")
database_name = os.environ.get("DATABASE_NAME")

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = f"{database_scheme}{database_user}@{database_address}:{database_port}/{database_name}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

init_db(app, db)
ma = Marshmallow(app)

app.register_blueprint(customer)

def create_tables():
    with app.app_context():
        print("Creating tables...")
        db.create_all()
        print("Tables created successfully")


create_tables()

if __name__ == '__main__':
    app.run(host=flask_host, port=flask_port)
