from django.contrib.auth import login
from django.shortcuts import render
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import MyTokenObtainPairSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    """
    View for TokenObtainPairView that also logs the user into a Django session.
    """

    serializer_class = MyTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if response.status_code == status.HTTP_200_OK:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.user

            login(request, user)

        return response


def login_view(request):
    return render(request, 'login.html')
