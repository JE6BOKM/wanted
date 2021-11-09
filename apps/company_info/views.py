from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.company_info.models import CompanyName
from apps.company_info.serializers import CompanyListSerializer


class CompanySearchView(APIView):
    """Company search view with query"""

    def get(self, request):
        name = request.GET.get("query", None)
        language = request.META.get("HTTP_X_WANTED_LANGUAGE")

        company_list = CompanyName.objects.filter(
            language__name=language, name__icontains=name
        )
        print(company_list)
        print(len(company_list))
        if len(company_list) == 0:
            return Response(
                {"error": f"There is no company with that name like {name}.  "},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = CompanyListSerializer(company_list, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
