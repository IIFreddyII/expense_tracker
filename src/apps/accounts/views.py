from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import MyTokenObtainPairSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    """
    View for TokenObtainPairView
    """

    serializer_class = MyTokenObtainPairSerializer


def login_view(request):
    return render(request, 'login.html')
