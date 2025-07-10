from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.views.generic import TemplateView
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Category
from .models import Transaction
from .serializers import CategorySerializer
from .serializers import TransactionSerializer


class CategoryViewSet(ModelViewSet):
    """
    ViewSet for Category model
    """

    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)


class TransactionViewSet(ModelViewSet):
    """
    ViewSet for Transaction model
    """

    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

    def _get_total_by_type(self, transaction_type: str) -> float:
        """
        Helper method to calculate the total amount for a given transaction type.
        """

        # Get transactions for the user and filter by the specified type.
        transactions = self.get_queryset().filter(type=transaction_type)

        # Aggregate the sum of the 'amount' field.
        total = transactions.aggregate(total=Sum('amount'))['total']

        # Return the total, or 0 if the total is None (no transactions found).
        return total or 0

    @action(detail=False, methods=['get'], url_path='total-expenses')
    def total_expenses(self, request):
        """
        Calculates and returns the total expenses for the authenticated user.
        """

        total = self._get_total_by_type('expense')

        return Response({'total_expenses': total})

    @action(detail=False, methods=['get'], url_path='total-incomes')
    def total_incomes(self, request):
        """
        Calculates and returns the total income for the authenticated user.
        """

        total = self._get_total_by_type('incomes')

        return Response({'total_incomes': total})


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'
