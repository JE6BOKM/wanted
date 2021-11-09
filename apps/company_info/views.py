from django.db.models.query import Prefetch

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.company_info.models import CompanyName, Tag, Language
from apps.company_info.serializers import (
    CompanyCreateSerializer,
    CompanyDetailSerializer,
    CompanyListSerializer,
    CompanyNameCreateSerializer,
)


class CompanyCreateView(APIView):
    def language_exist_or_create(self, languages):
        """Check language exist and Create."""
        for name in languages:
            try:
                Language.objects.get(name=name)
                # print(f"{name} is OK.")
            except Language.DoesNotExist:
                Language.objects.create(name=name)
                # print(f"{name} is Created.")

    def tag_exist_or_create(self, tag_list):
        self._tag_object_list = []
        for tags in tag_list:
            for language, tag_name in tags.get("tag_name").items():
                try:
                    language_obj = Language.objects.get(name=language)
                    tag_obj = Tag.objects.get(
                        name=tag_name, language=language_obj
                    )
                    self._tag_object_list.append(tag_obj.id)
                except Tag.DoesNotExist:
                    tag_data = {"name": tag_name, "language": language_obj}
                    tag_obj = Tag.objects.create(**tag_data)
                    self._tag_object_list.append(tag_obj.id)
                except Language.DoesNotExist:
                    return Response(status=status.HTTP_400_BAD_REQUEST)

    def company_create(self, company_data):
        company_serializer = CompanyCreateSerializer(data=company_data)
        if company_serializer.is_valid():
            # company name create
            company = company_serializer.save()
            return company

    def generate_company_name_data(self, language_name, company_name, company):
        try:
            language = Language.objects.get(name=language_name)
        except Language.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            company_name_data = {
                "name": company_name,
                "language": language.id,
                "c_id": company.id,
            }
            return company_name_data

    def company_name_create(self, company_name_data):
        company_name_create_serializer = CompanyNameCreateSerializer(
            data=company_name_data
        )
        if company_name_create_serializer.is_valid():
            new_company_name = company_name_create_serializer.save()
            return new_company_name

    def post(self, request):
        language = request.META.get("HTTP_X_WANTED_LANGUAGE")
        company_name_list = request.data.get("company_name")
        tag_list = request.data.get("tags")
        language_list = company_name_list.keys()

        # check language exist or create
        self.language_exist_or_create(language_list)
        # check tag exist or create
        self.tag_exist_or_create(tag_list)
        # company create
        company_data = {"tags": self._tag_object_list}

        company = self.company_create(company_data)
        for language_name, company_name in company_name_list.items():
            company_name_data = self.generate_company_name_data(
                language_name, company_name, company
            )
            new_company_name = self.company_name_create(company_name_data)

            if new_company_name.language.name == language:
                result = new_company_name.id
                result_company = CompanyName.objects.prefetch_related(
                    Prefetch(
                        "c_id__tags",
                        queryset=Tag.objects.filter(language__name=language),
                    )
                )
                result_company = result_company.get(id=result)
                result_serializer = CompanyDetailSerializer(result_company)
                return Response(
                    data=result_serializer.data, status=status.HTTP_200_OK
                )
        return Response(status=status.HTTP_400_BAD_REQUEST)


class CompanyNameDetailView(APIView):
    def get(self, request, name):
        language = request.META.get("HTTP_X_WANTED_LANGUAGE")
        try:
            CompanyName.objects.get(name=name)
            company = CompanyName.objects.prefetch_related(
                Prefetch(
                    "c_id__tags",
                    queryset=Tag.objects.filter(language__name=language),
                )
            )
            company = company.get(language__name=language, name=name)
        except CompanyName.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CompanyDetailSerializer(company)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CompanySearchView(APIView):
    """Company search view with query"""

    def get(self, request):
        name = request.GET.get("query", None)
        language = request.META.get("HTTP_X_WANTED_LANGUAGE")

        company_list = CompanyName.objects.filter(
            language__name=language, name__icontains=name
        )
        if len(company_list) == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CompanyListSerializer(company_list, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
