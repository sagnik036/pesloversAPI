# Common Imports
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
# Module Imports
from api.common.serializers.serializers import MasterListFilterBackend
from api.common.responses.error_response import FormatResponses
from .services import *
from .serializers import *


class PlayerView(GenericAPIView):
    serializer_class = PlayerSerializers
    filter_backends = (MasterListFilterBackend,)
  
    @classmethod
    def get(cls, request):
        data = request.GET
        response = PlayerServices.fetch_profiles(data)
        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)

    @classmethod
    def post(cls, request):
        validate_data = PlayerSerializers(data=request.data)
        is_valid = validate_data.is_valid()
        if is_valid:
            data = validate_data.validated_data
            instance = PlayerServices.save(data)
            response = {
                "result": instance.id,
                "message": "Player Added successfully."
            }
            status_code = status.HTTP_200_OK
        else:
            errors = FormatResponses.error_response(validate_data.errors)
            response = {"errors": errors}
            status_code = status.HTTP_400_BAD_REQUEST
        return Response(response, status=status_code)


class PlayerDetailView(GenericAPIView):
    serializer_class = PlayerSerializers
    filter_backends = (MasterListFilterBackend,)

    @classmethod
    def get(cls, request, pk):
        response = PlayerServices.fetchProfileById(pk)
        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)

    @classmethod
    def put(cls, request, pk):
        validate_date = PlayerSerializers(data=request.data)
        is_valid = validate_date.is_valid()
        if is_valid:
            data = validate_date.validated_data
            PlayerServices.update(pk, data)
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
        PlayerServices.delete(pk)
        response = {
            "message": "Deleted Successfully"
        }
        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)
