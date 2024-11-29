from datetime import timedelta

from django.db import models
from agro_marketplace.accounts.models import Profile
from agro_marketplace.choises import Currency, UnitOfMeasure, PriceTypeChoices, Category
from agro_marketplace.validators import FileSizeValidator
from django.utils import timezone


class BuyerItems(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='buyer_products'
    )
    title = models.CharField(
        max_length=255
    )
    category = models.CharField(
        max_length=20,
        choices=Category.choices
    )
    location = models.CharField(
        max_length=255
    )
    description = models.TextField()
    photo_1 = models.ImageField(
        upload_to="buyer_items/",
        validators=[FileSizeValidator(5),],
        blank=True,
        null=True,
    )
    photo_2 = models.ImageField(
        upload_to="buyer_items/",
        validators=[FileSizeValidator(5),],
        blank=True,
        null=True,
    )
    photo_3 = models.ImageField(
        upload_to="buyer_items/",
        validators=[FileSizeValidator(5),],
        blank=True,
        null=True,
    )
    photo_4 = models.ImageField(
        upload_to="buyer_items/",
        validators=[FileSizeValidator(5),],
        blank=True,
        null=True,
    )
    phone = models.CharField(
        max_length=15,
        null=True,
        blank=True
    )
    quantity = models.PositiveIntegerField()
    price_type = models.CharField(
        max_length=20,
        choices=PriceTypeChoices.choices,
        default=PriceTypeChoices.NEGOTIATION,
    )
    price_per_unit = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    price_all_quantity = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    currency = models.CharField(
        max_length=3,
        choices=Currency.choices,
        default=Currency.LEVA,
    )

    unit_of_measure = models.CharField(
        max_length=3,
        choices=UnitOfMeasure.choices,
        default=UnitOfMeasure.KG,
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    # Store the expiration date directly
    expiration_date = models.DateTimeField(
        null=True, blank=True, editable=False
    )

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()
        self.expiration_date = self.created_at + timedelta(days=30)

        super().save(*args, **kwargs)

    def stringify(self):
        # Return a string formatted as pk_title
        return f"{self.pk}_{self.title.replace(' ', '_').lower()}"

    def __str__(self):
        return self.stringify()
