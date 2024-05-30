"""
Individual projects need to subclass it and implement a few methods and may include any extra
payment-related fields on this model. It is also possible to add a foreign key to an existing
purchase or order model.
"""

from decimal import Decimal
from typing import NamedTuple, Iterable

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.translation import pgettext_lazy
from phonenumber_field.modelfields import PhoneNumberField


class FraudStatus:
    UNKNOWN = "unknown"
    ACCEPT = "accept"
    REJECT = "reject"
    REVIEW = "review"

    CHOICES = [
        (UNKNOWN, pgettext_lazy("fraud status", "Unknown")),
        (ACCEPT, pgettext_lazy("fraud status", "Passed")),
        (REJECT, pgettext_lazy("fraud status", "Rejected")),
        (REVIEW, pgettext_lazy("fraud status", "Review")),
    ]


class PaymentStatus:
    WAITING = "waiting"
    PREAUTH = "preauth"
    CONFIRMED = "confirmed"
    REJECTED = "rejected"
    REFUNDED = "refunded"
    ERROR = "error"
    INPUT = "input"

    CHOICES = [
        (WAITING, pgettext_lazy("payment status", "Waiting for confirmation")),
        (PREAUTH, pgettext_lazy("payment status", "Pre-authorized")),
        (CONFIRMED, pgettext_lazy("payment status", "Confirmed")),
        (REJECTED, pgettext_lazy("payment status", "Rejected")),
        (REFUNDED, pgettext_lazy("payment status", "Refunded")),
        (ERROR, pgettext_lazy("payment status", "Error")),
        (INPUT, pgettext_lazy("payment status", "Input")),
    ]


class BasePayment(models.Model):
    """
    Represents a single transaction. Each instance has one or more PaymentItem.
    """

    variant = models.CharField(max_length=255)
    #: Transaction status
    status = models.CharField(
        max_length=10, choices=PaymentStatus.CHOICES, default=PaymentStatus.WAITING
    )
    fraud_status = models.CharField(
        _("fraud check"),
        max_length=10,
        choices=FraudStatus.CHOICES,
        default=FraudStatus.UNKNOWN,
    )
    fraud_message = models.TextField(blank=True, default="")
    #: Creation date and time
    created = models.DateTimeField(auto_now_add=True)
    #: Date and time of last modification
    modified = models.DateTimeField(auto_now=True)
    #: Transaction ID (if applicable)
    transaction_id = models.CharField(max_length=255, blank=True)
    #: Currency code (may be provider-specific)
    currency = models.CharField(max_length=10)
    #: Total amount (gross)
    total = models.DecimalField(max_digits=9, decimal_places=2, default="0.0")
    delivery = models.DecimalField(max_digits=9, decimal_places=2, default="0.0")
    tax = models.DecimalField(max_digits=9, decimal_places=2, default="0.0")
    description = models.TextField(blank=True, default="")
    billing_first_name = models.CharField(max_length=256, blank=True)
    billing_last_name = models.CharField(max_length=256, blank=True)
    billing_address_1 = models.CharField(max_length=256, blank=True)
    billing_address_2 = models.CharField(max_length=256, blank=True)
    billing_city = models.CharField(max_length=256, blank=True)
    billing_postcode = models.CharField(max_length=256, blank=True)
    billing_country_code = models.CharField(max_length=2, blank=True)
    billing_country_area = models.CharField(max_length=256, blank=True)
    billing_email = models.EmailField(blank=True)
    billing_phone = PhoneNumberField(blank=True)
    customer_ip_address = models.GenericIPAddressField(blank=True, null=True)
    extra_data = models.TextField(blank=True, default="")
    message = models.TextField(blank=True, default="")
    token = models.CharField(max_length=36, blank=True, default="")
    captured_amount = models.DecimalField(max_digits=9, decimal_places=2, default="0.0")


class PurchasedItem(NamedTuple):
    """A single item in a purchase."""

    name: str
    quantity: int
    price: Decimal
    currency: str
    sku: str
    tax_rate: Decimal | None = None


class Payment(BasePayment):

    def get_failure_url(self) -> str:
        # Return a URL where users are redirected after
        # they fail to complete a payment:
        return f"http://example.com/payments/{self.pk}/failure"

    def get_success_url(self) -> str:
        # Return a URL where users are redirected after
        # they successfully complete a payment:
        return f"http://example.com/payments/{self.pk}/success"

    def get_purchased_items(self) -> Iterable[PurchasedItem]:
        # Return items that will be included in this payment.
        yield PurchasedItem(
            name="The Hound of the Baskervilles",
            sku="BSKV",
            quantity=9,
            price=Decimal(10),
            currency="USD",
        )
