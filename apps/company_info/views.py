from typing import List

from django.db.models.query import Prefetch

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.company_info.models import CompanyName, Language, Tag
from apps.company_info.serializers import CompanyDetailSerializer, CompanyListSerializer


class CompanyCreateView(APIView):
    def language_exist_or_create(self, languages: List):
        for name in languages:
            try:
                Language.objects.get(name=name)
                print(f"{name} is OK.")
            except Language.DoesNotExist:
                Language.objects.create(name=name)
                print(f"{name} is Created.")

    def post(self, request):
        print(dir(request.data))

        company_name = request.data.get("company_name")
        # tags = request.data.get("tags")
        language_list = company_name.keys()
        self.language_exist_or_create(language_list)
        for company_name, language_name in company_name.items():
            pass

        return Response(status=status.HTTP_200_OK)


class CompanyNameDetailView(APIView):
    def get(self, request, name):
        language = request.META.get("HTTP_X_WANTED_LANGUAGE")
        company_name = CompanyName.objects.get(name=name)
        if not company_name:
            return Response(status=status.HTTP_404_NOT_FOUND)
        # company = CompanyName.objects.get(language__name=language, name=name)
        company = CompanyName.objects.prefetch_related(
            Prefetch(
                "c_id__tags",
                queryset=Tag.objects.filter(language__name=language),
            )
        )
        company = company.get(language__name=language, name=name)

        serializer = CompanyDetailSerializer(company)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CompanySearchView(APIView):
    def get(self, request):
        name = request.GET.get("query", None)
        language = request.META.get("HTTP_X_WANTED_LANGUAGE")

        company_list = CompanyName.objects.filter(
            language__name=language, name__contains=name
        )
        serializer = CompanyListSerializer(company_list, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
