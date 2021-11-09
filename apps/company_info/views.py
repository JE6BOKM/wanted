from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.company_info.models import CompanyName
from apps.company_info.serializers import CompanyListSerializer


class CompanyCreateView(APIView):
    """Company Create View"""

    def post(self, request):
        pass


class CompanySearchView(APIView):
    def get(self, request):
        name = request.GET.get("query", None)
        language = request.META.get("HTTP_X_WANTED_LANGUAGE")

        company_list = CompanyName.objects.filter(
            language__name=language, name__contains=name
        )
        serializer = CompanyListSerializer(company_list, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
