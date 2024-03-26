import uuid
from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma

from db import db


class Product(db.Model):
    __tablename__ = "Product"

    product_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    price = db.Column(db.Float(), nullable=False)
    stock_quantity = db.Column(db.Integer(), nullable=False)

    def __init__(self, name, description, price, stock_quantity):
        self.name = name
        self.description = description
        self.price = price
        self.stock_quantity = stock_quantity


class ProductSchema(ma.Schema):
    class Meta:
        fields = ['product_id', 'name', 'description', 'price', 'stock_quantity']


product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
