from django.db.models.query import Prefetch

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.company_info.models import CompanyName, Tag
from apps.company_info.serializers import CompanyDetailSerializer


class CompanyNameDetailView(APIView):
    def get(self, request, name):
        language = request.META.get("HTTP_X_WANTED_LANGUAGE")
        company_name = CompanyName.objects.get(name=name)
        if not company_name:
            return Response(status=status.HTTP_404_NOT_FOUND)
        company = CompanyName.objects.prefetch_related(
            Prefetch(
                "c_id__tags",
                queryset=Tag.objects.filter(language__name=language),
            )
        )
        company = company.get(language__name=language, name=name)

        serializer = CompanyDetailSerializer(company)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
