from django.contrib import admin

from .models import Category, Transaction


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "created_at", "name", "user"]
    list_filter = ["created_at"]
    search_fields = ["name"]
    autocomplete_fields = ["user"]


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ["id", "created_at", "user", "category", "date", "amount", "description"]
    list_filter = ["created_at", "type"]
    search_fields = ["description"]
    autocomplete_fields = ["user", "category"]
