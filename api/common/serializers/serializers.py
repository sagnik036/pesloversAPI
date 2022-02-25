from rest_framework import serializers
from rest_framework.filters import BaseFilterBackend
import coreapi


class MasterListSerializers(serializers.Serializer):
    search = serializers.CharField(
        required=False,
        allow_blank=True
    )
    limit = serializers.IntegerField(
        required=False,
        allow_null=True,
        default=10
    )
    page = serializers.IntegerField(
        required=False,
        allow_null=True,
        default=1
    )
    expand = serializers.CharField(
        required=False,
        allow_blank=True,
        default="",
        help_text="Pass values with comma separated."
    )

    @classmethod
    def validate(cls, data):
        errors = {}

        if errors:
            raise serializers.ValidationError(data)
        return super(MasterListSerializers, cls).validate(cls, data)


class MasterListFilterBackend(BaseFilterBackend):
    @classmethod
    def get_schema_fields(cls, view):
        params = [
            coreapi.Field(
                name='search',
                location='query',
                required=False,
                type='string',
                description='''
                    Pass search keywords in this field.
                    Items will be searched with this keywords by Contains method.
                '''
            ),
            coreapi.Field(
                name='page_size',
                location='query',
                required=False,
                type="integer",
                description='''
                    Pass how many items you want show in one page.
                    Type of this field is Integer and minimum value is 1.
                    default limit is 10.
                '''
            )
        ]
        return params


class MasterExpandFilterBackend(BaseFilterBackend):
    @classmethod
    def get_schema_fields(cls, view):
        params = [
            coreapi.Field(
                name='expands',
                location='query',
                required=False,
                type='string',
                description='''
                    Pass expand parameters with comma separated. For options contact developer.
                '''
            )
        ]
        return params


class VoidSerializers(serializers.Serializer):
    @classmethod
    def validate(cls, data):
        errors = {}

        if errors:
            raise serializers.ValidationError(errors)
        return super(VoidSerializers, cls).validate(cls, data)
