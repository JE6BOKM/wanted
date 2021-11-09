from django.urls import path

from apps.company_info.views import (
    CompanyCreateView,
    CompanyNameDetailView,
    CompanySearchView,
)

app_name = "companies"

urlpatterns = [
    path("companies", CompanyCreateView.as_view()),
    path("companies/<str:name>", CompanyNameDetailView.as_view()),
    path("search", CompanySearchView.as_view()),
]
