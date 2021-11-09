from rest_framework.serializers import CharField, ModelSerializer, StringRelatedField

from apps.company_info.models import CompanyName


class CompanyListSerializer(ModelSerializer):
    company_name = CharField(source="name")

    class Meta:
        model = CompanyName
        fields = ("company_name",)


class CompanyDetailSerializer(ModelSerializer):
    company_name = CharField(source="name")
    tags = StringRelatedField(many=True, source="c_id.tags")

    class Meta:
        model = CompanyName
        fields = ("company_name", "tags")