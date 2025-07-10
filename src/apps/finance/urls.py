from django.urls import path
from django.contrib.auth import views as auth_views

from .views import DashboardView

urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
