# encoding: utf-8
"""
Customers module
============
"""

from app.extensions.api import api_v1


def init_app(app, **kwargs):
    # pylint: disable=unused-argument,unused-variable
    """
    Init Customers module.
    """
    api_v1.add_oauth_scope('customers:read', "Provide access to Customers details")
    api_v1.add_oauth_scope('customers:write', "Provide write access to Customers details")

    # Touch underlying modules
    from . import models, resources

    api_v1.add_namespace(resources.api)