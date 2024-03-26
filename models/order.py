import uuid
from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma

from db import db


class Order(db.Model):
    __tablename__ = "Order"

    order_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    customer_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Customer.customer_id"), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    total_amount = db.Column(db.Float(), nullable=False)
    status = db.Column(db.String(), nullable=False)

    customer = db.relationship("Customer", foreign_keys='[Customer.customer_id]', back_populates='order')

    def __init__(self, customer_id, date, total_amount, status):
        self.customer_id = customer_id
        self.date = date
        self.total_amount = total_amount
        self.status = status


class OrderSchema(ma.Schema):
    class Meta:
        fields = ['order_id', 'customer_id', 'date', 'total_amount', 'status', 'customer']
        customer = ma.fields.Nested("CustomerSchema", many=True)


order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)
