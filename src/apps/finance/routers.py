from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, TransactionViewSet

FINANCE_ROUTER = DefaultRouter()
FINANCE_ROUTER.register("categories", CategoryViewSet, basename="categories")
FINANCE_ROUTER.register("transactions", TransactionViewSet, basename="transactions")

urlpatterns = [
    path("", include(FINANCE_ROUTER.urls)),
]
