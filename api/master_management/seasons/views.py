# Common Imports
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
# Module Imports
from api.common.serializers.serializers import MasterListFilterBackend
from api.common.responses.error_response import FormatResponses
from .services import *
from .serializers import *


class SeasonView(GenericAPIView):
    serializer_class = SeasonSerializers
    filter_backends = (MasterListFilterBackend,)
  
    @classmethod
    def get(cls, request):
        data = request.GET
        response = SeasonServices.fetch_profiles(data)
        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)

    @classmethod
    def post(cls, request):
        validate_data = SeasonSerializers(data=request.data)
        is_valid = validate_data.is_valid()
        if is_valid:
            data = validate_data.validated_data
            instance = SeasonServices.save(data)
            response = {
                "result": instance.id,
                "message": "Season Added successfully."
            }
            status_code = status.HTTP_200_OK
        else:
            errors = FormatResponses.error_response(validate_data.errors)
            response = {"errors": errors}
            status_code = status.HTTP_400_BAD_REQUEST
        return Response(response, status=status_code)


class SeasonDetailView(GenericAPIView):
    serializer_class = SeasonSerializers
    filter_backends = (MasterListFilterBackend,)

    @classmethod
    def get(cls, request, user_code):
        response = SeasonServices.fetchProfileById(user_code)
        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)

    @classmethod
    def put(cls, request, user_code):
        validate_date = SeasonSerializers(data=request.data)
        is_valid = validate_date.is_valid()
        if is_valid:
            data = validate_date.validated_data
            SeasonServices.update(user_code, data)
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
    def delete(cls, request, user_code):
        SeasonServices.delete(user_code)
        response = {
            "message": "Deleted Successfully"
        }
        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)
