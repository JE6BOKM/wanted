from django.urls import path

from apps.company_info.views import CompanyNameDetailView

app_name = "companies"

urlpatterns = [
    path("companies/<str:name>", CompanyNameDetailView.as_view()),
]
