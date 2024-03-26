import uuid
from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma

from db import db


class ProductCategory(db.Model):
    __tablename__ = "ProductCategory"

    category_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(), nullable=False)

    def __init__(self, name):
        self.name = name


class ProductCategorySchema(ma.Schema):
    class Meta:
        fields = ['category_id', 'name']


product_category_schema = ProductCategorySchema()
product_categories_schema = ProductCategorySchema(many=True)
