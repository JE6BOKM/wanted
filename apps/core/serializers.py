from rest_framework import serializers


class DynamicFieldsSerializerMixin(serializers.Serializer):
    """
    Dynamically modifying fields
    https://www.django-rest-framework.org/api-guide/serializers/#dynamically-modifying-fields
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        ##################
        # Inspired by:
        # https://medium.com/@Joelhanson25/advanced-serializer-usage-dynamically-modifying-fields-e7c3bc28efa6
        # request의 query string으로 필요한 fields값이 들어오면 해당 fields만 담긴
        # 응답을 return한다.
        ##################
        if request := kwargs.get("context", {}).get("request"):
            if str_fields := request.GET.get("fields", ""):
                kwargs["fields"] = str_fields.split(",")

        #############
        # In DRF docs
        #############
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop("fields", None)

        # Instantiate the superclass normally
        super(DynamicFieldsSerializerMixin, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class ChooseSerializerClassMixin:
    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)
