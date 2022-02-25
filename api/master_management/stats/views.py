# Common Imports
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
# Module Imports
from api.common.serializers.serializers import MasterListFilterBackend
from api.common.responses.error_response import FormatResponses
from .services import *
from .serializers import *


class StatsView(GenericAPIView):
    serializer_class = StatsSerializers
    filter_backends = (MasterListFilterBackend,)
  
    @classmethod
    def get(cls, request):
        data = request.GET
        response = StatServices.fetch_profiles(data)
        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)

    @classmethod
    def post(cls, request):
        validate_data = StatsSerializers(data=request.data)
        is_valid = validate_data.is_valid()
        if is_valid:
            data = validate_data.validated_data
            instance = StatServices.save(data)
            response = {
                "result": instance.id,
                "message": "Stats Added successfully."
            }
            status_code = status.HTTP_200_OK
        else:
            errors = FormatResponses.error_response(validate_data.errors)
            response = {"errors": errors}
            status_code = status.HTTP_400_BAD_REQUEST
        return Response(response, status=status_code)


class StatsDetailView(GenericAPIView):
    serializer_class = StatsSerializers
    filter_backends = (MasterListFilterBackend,)

    @classmethod
    def get(cls, request, pk):
        response = StatServices.fetchProfileById(pk)
        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)

    @classmethod
    def put(cls, request, pk):
        validate_date = StatsSerializers(data=request.data)
        is_valid = validate_date.is_valid()
        if is_valid:
            data = validate_date.validated_data
            StatServices.update(pk, data)
            response = {
                "message": "Updated Successfully"
            }
            status_code = status.HTTP_200_OK
            return Response(response, status=status_code)

        else:
            errors = FormatResponses.error_response(validate_date.errors)
            response = {
                "errors": errors
            }
            status_code = status.HTTP_400_BAD_REQUEST
            return Response(response, status_code)

    @classmethod
    def delete(cls, request, pk):
        StatServices.delete(pk)
        response = {
            "message": "Deleted Successfully"
        }
        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)
