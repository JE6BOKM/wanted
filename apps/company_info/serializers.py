from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, StringRelatedField

from apps.company_info.models import CompanyName


class CompanyNameWriteSerializer(ModelSerializer):
    class Meta:
        model = CompanyName
        fields = ("__all__",)


# class CompanySerializer(ModelSerializer):
#     tags = StringRelatedField(many=True, read_only=True)
#     company_name = StringRelatedField(many=True, read_only=True)

#     class Meta:
#         model = Company
#         fields = ("company_name", "tags")


class CompanyListSerializer(ModelSerializer):
    company_name = serializers.CharField(source="name")

    class Meta:
        model = CompanyName
        fields = ("company_name",)


class CompanyDetailSerializer(ModelSerializer):
    company_name = serializers.CharField(source="name")
    tags = StringRelatedField(many=True, source="c_id.tags")

    class Meta:
        model = CompanyName
        fields = ("company_name", "tags")
