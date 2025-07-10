from django.urls import include, path

urlpatterns = [
    path("", include("apps.accounts.urls")),
    path("dashboard/", include("apps.finance.urls")),
]
