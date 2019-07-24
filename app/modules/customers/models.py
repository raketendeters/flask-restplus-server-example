# encoding: utf-8
"""
Customers database models
--------------------
"""

from sqlalchemy_utils import Timestamp

from app.extensions import db


class Customer(db.Model, Timestamp):
    """
    Customers database model.
    """
    # pylint: disable=invalid-name
    id = db.Column(db.Integer, primary_key=True)  # pylint: disable=invalid-name
    title = db.Column(db.String(length=250), nullable=False)
    customer_number = db.Column(db.String(length=250), unique=True)
    customer_id = db.Column(db.String(length=250), unique=True)
    days_for_payment = db.Column(db.Integer)
    payment_type = db.Column(db.String(length=200), nullable=True)
    bank_name = db.Column(db.String(length=200), nullable=True)
    bank_account_number = db.Column(db.String(length=200), nullable=True)
    bank_code = db.Column(db.String(length=200), nullable=True)
    bank_account_owner = db.Column(db.String(length=200), nullable=True)
    bank_iban = db.Column(db.String(length=200), nullable=True)
    bank_bic = db.Column(db.String(length=200), nullable=True)
    bank_account_mandate_reference = db.Column(db.String(length=200), nullable=True)
    show_payment_notice = db.Column(db.Boolean, default=1)
    account_receivable = db.Column(db.String(length=200), nullable=True)
    customer_type = db.Column(db.String(length=200), nullable=True)
    top = db.Column(db.String(length=200), nullable=True)
    newsletter_optin = db.Column(db.Boolean, default=1)
    organization = db.Column(db.String(length=200), nullable=True)
    position = db.Column(db.String(length=200), nullable=True)
    academic_degree = db.Column(db.String(length=200), nullable=True)
    salutation = db.Column(db.String(length=200), nullable=True)
    first_name = db.Column(db.String(length=200), nullable=True)
    last_name = db.Column(db.String(length=200), nullable=True)
    address = db.Column(db.String(length=200), nullable=True)
    address_2 = db.Column(db.String(length=200), nullable=True)
    zipcode = db.Column(db.String(length=200), nullable=True)
    city = db.Column(db.String(length=200), nullable=True)
    country_code = db.Column(db.String(length=200), nullable=True)
    secondary_address = db.Column(db.String(length=200), nullable=True)
    phone = db.Column(db.String(length=200), nullable=True)
    phone_2 = db.Column(db.String(length=200), nullable=True)
    fax = db.Column(db.String(length=200), nullable=True)
    mobile = db.Column(db.String(length=200), nullable=True)
    email = db.Column(db.String(length=200), nullable=True)
    website = db.Column(db.String(length=200), nullable=True)
    vat_id = db.Column(db.String(length=200), nullable=True)
    currency_code = db.Column(db.String(length=200), nullable=True)
    tags = db.Column(db.String(length=200), nullable=True)
    created_on_fb = db.Column(db.String(length=200), nullable=True)

    def __repr__(self):
        return (
            "<{class_name}("
            "id={self.id}, "
            "title=\"{self.title}\""
            ")>".format(
                class_name=self.__class__.__name__,
                self=self
            )
        )

    @db.validates('title')
    def validate_title(self, key, title):  # pylint: disable=unused-argument,no-self-use
        if len(title) < 3:
            raise ValueError("Title has to be at least 3 characters long.")
        return title
