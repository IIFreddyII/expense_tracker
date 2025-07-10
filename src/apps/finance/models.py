from base.models import BaseModel
from django.contrib.auth.models import User
from django.db import models


class Category(BaseModel):
    """
    Model for categories
    """

    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class Transaction(BaseModel):
    """
    Model for transactions
    """

    TRANSACTION_TYPES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'transaction'
        verbose_name_plural = 'transactions'
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        """
        Overrides the save method to convert the description to uppercase.
        """

        if self.description:
            self.description = self.description.upper()
        super(Transaction, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.description} - {self.amount}"
