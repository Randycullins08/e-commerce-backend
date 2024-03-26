import uuid
from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma

from db import db


class Customer(db.Model):
    __tablename__ = "Customer"

    customer_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)
    address = db.Column(db.String(), nullable=False)
    phone = db.Column(db.String(), nullable=False)

    def __init__(self, name, email, address, phone):
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone


class CustomerSchema(ma.Schema):
    class Meta:
        fields = ['customer_id', 'name', 'email', 'address', 'phone']


customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)
