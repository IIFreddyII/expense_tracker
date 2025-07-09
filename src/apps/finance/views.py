from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Category, Transaction
from .serializers import CategorySerializer, TransactionSerializer


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


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')
