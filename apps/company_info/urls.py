from django.urls import path

from apps.company_info.views import CompanyNameDetailView, CompanySearchView

app_name = "companies"

urlpatterns = [
    path("search", CompanySearchView.as_view()),
    path("companies/<str:name>", CompanyNameDetailView.as_view()),
]
