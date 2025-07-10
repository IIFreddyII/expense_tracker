from rest_framework import serializers
from .models import Transaction, Category


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for Category model
    """

    class Meta:
        model = Category
        read_only_fields = ["id", "created_at", "updated_at", "user"]
        fields = [*read_only_fields, "name"]


class TransactionSerializer(serializers.ModelSerializer):
    """
    Serializer for Transaction model
    """

    class Meta:
        model = Transaction
        read_only_fields = ["id", "created_at", "updated_at"]
        fields = [*read_only_fields, "category", "description", "amount", "type", "date", "user"]
