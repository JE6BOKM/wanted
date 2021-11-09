from django.urls import path

from apps.company_info.views import CompanySearchView

app_name = "companies"

urlpatterns = [
    path("search", CompanySearchView.as_view()),
]
