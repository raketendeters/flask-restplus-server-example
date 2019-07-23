# encoding: utf-8
# pylint: disable=bad-continuation
"""
RESTful API Customers resources
--------------------------
"""

import logging

from flask_login import current_user
from flask_restplus_patched import Resource
from flask_restplus._http import HTTPStatus

from app.extensions import db
from app.extensions.api import Namespace, abort
from app.extensions.api.parameters import PaginationParameters
from app.modules.users import permissions


from . import parameters, schemas
from .models import Customer


log = logging.getLogger(__name__)  # pylint: disable=invalid-name
api = Namespace('customers', description="Customers")  # pylint: disable=invalid-name


@api.route('/')
@api.login_required(oauth_scopes=['customers:read'])
class Customers(Resource):
    """
    Manipulations with Customers.
    """

    @api.parameters(PaginationParameters())
    @api.response(schemas.BaseCustomerSchema(many=True))
    def get(self, args):
        """
        List of Customer.

        Returns a list of Customer starting from ``offset`` limited by ``limit``
        parameter.
        """
        return Customer.query.offset(args['offset']).limit(args['limit'])

    @api.login_required(oauth_scopes=['customers:write'])
    @api.parameters(parameters.CreateCustomerParameters())
    @api.response(schemas.DetailedCustomerSchema())
    @api.response(code=HTTPStatus.CONFLICT)
    def post(self, args):
        """
        Create a new instance of Customer.
        """
        with api.commit_or_abort(
                db.session,
                default_error_message="Failed to create a new Customer"
            ):
            customer = Customer(**args)
            db.session.add(customer)
        return customer


@api.route('/<int:customer_id>')
@api.login_required(oauth_scopes=['customers:read'])
@api.response(
    code=HTTPStatus.NOT_FOUND,
    description="Customer not found.",
)
@api.resolve_object_by_model(Customer, 'customer')
class CustomerByID(Resource):
    """
    Manipulations with a specific Customer.
    """

    @api.response(schemas.DetailedCustomerSchema())
    def get(self, customer):
        """
        Get Customer details by ID.
        """
        return customer

    @api.login_required(oauth_scopes=['customers:write'])
    @api.permission_required(permissions.WriteAccessPermission())
    @api.parameters(parameters.PatchCustomerDetailsParameters())
    @api.response(schemas.DetailedCustomerSchema())
    @api.response(code=HTTPStatus.CONFLICT)
    def patch(self, args, customer):
        """
        Patch Customer details by ID.
        """
        with api.commit_or_abort(
                db.session,
                default_error_message="Failed to update Customer details."
            ):
            parameters.PatchCustomerDetailsParameters.perform_patch(args, obj=customer)
            db.session.merge(customer)
        return customer

    @api.login_required(oauth_scopes=['customers:write'])
    @api.permission_required(permissions.WriteAccessPermission())
    @api.response(code=HTTPStatus.CONFLICT)
    @api.response(code=HTTPStatus.NO_CONTENT)
    def delete(self, customer):
        """
        Delete a Customer by ID.
        """
        with api.commit_or_abort(
                db.session,
                default_error_message="Failed to delete the Customer."
            ):
            db.session.delete(customer)
        return None