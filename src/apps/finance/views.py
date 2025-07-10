from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render
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

    @action(detail=False, methods=['get'], url_path='total-expenses')
    def total_expenses(self, request):
        """
        A custom action to calculate the sum of all 'expense' transactions
        for the authenticated user.
        """

        user_transactions = self.get_queryset()
        user_expenses = user_transactions.filter(type='expense')

        total = user_expenses.aggregate(total_amount=Sum('amount'))['total_amount']

        if total is None:
            total = 0

        return Response({'total_expenses': total})

    @action(detail=False, methods=['get'], url_path='total-incomes')
    def total_incomes(self, request):
        """
        A custom action to calculate the sum of all 'income' transactions
        for the authenticated user.
        """
        user_transactions = self.get_queryset()
        user_incomes = user_transactions.filter(type='income')

        total = user_incomes.aggregate(total_amount=Sum('amount'))['total_amount']

        if total is None:
            total = 0

        return Response({'total_incomes': total})


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')
