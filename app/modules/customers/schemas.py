# encoding: utf-8
"""
Serialization schemas for Customers resources RESTful API
----------------------------------------------------
"""

from flask_marshmallow import base_fields
from flask_restplus_patched import ModelSchema

from .models import Customer


class BaseCustomerSchema(ModelSchema):
    """
    Base Customer schema exposes only the most general fields.
    """

    class Meta:
        # pylint: disable=missing-docstring
        model = Customer
        fields = (
            Customer.id.key,
            Customer.title.key,
        )
        dump_only = (
            Customer.id.key,
        )


class DetailedCustomerSchema(BaseCustomerSchema):
    """
    Detailed Customer schema exposes all useful fields.
    """

    class Meta(BaseCustomerSchema.Meta):
        fields = BaseCustomerSchema.Meta.fields + (
            Customer.created.key,
            Customer.updated.key,
        )
        dump_only = BaseCustomerSchema.Meta.dump_only + (
            Customer.created.key,
            Customer.updated.key,
        )