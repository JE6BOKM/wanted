from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.company_info.models import CompanyName


class CompanyListSerializer(ModelSerializer):
    company_name = serializers.CharField(source="name")

    class Meta:
        model = CompanyName
        fields = ("company_name",)
