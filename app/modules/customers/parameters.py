# encoding: utf-8
"""
Input arguments (Parameters) for Customers resources RESTful API
-----------------------------------------------------------
"""

from flask_marshmallow import base_fields
from flask_restplus_patched import PostFormParameters, PatchJSONParameters

from . import schemas
from .models import Customer


class CreateCustomerParameters(PostFormParameters, schemas.DetailedCustomerSchema):

    class Meta(schemas.DetailedCustomerSchema.Meta):
        pass


class PatchCustomerDetailsParameters(PatchJSONParameters):
    # pylint: disable=abstract-method,missing-docstring
    OPERATION_CHOICES = (
        PatchJSONParameters.OP_REPLACE,
    )

    PATH_CHOICES = tuple(
        '/%s' % field for field in (
            Customer.title.key,
        )
    )