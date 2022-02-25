# Common Imports
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.parsers import MultiPartParser, FormParser
from api.common.responses.error_response import FormatResponses
from .serializers import FileUploadSerializer
from .services import MediaUploadServices


class MediaUploadView(GenericAPIView):
    serializer_class = FileUploadSerializer
    parser_classes = [FormParser, MultiPartParser]
    permission_classes = [AllowAny]

    @classmethod
    def post(cls, request, version):
        validate_data = FileUploadSerializer(data=request.data)
        is_valid = validate_data.is_valid()
        if is_valid:
            data = validate_data.validated_data
            file = data.get("file")
            result = MediaUploadServices.upload_to_cloudinary(
                file
            )
            response = {
                "message": "Media uploaded successfully.",
                "media_url": result
            }
            status_code = status.HTTP_200_OK
        else:
            errors = FormatResponses.error_response(validate_data.errors)
            response = {"errors": errors}
            status_code = status.HTTP_400_BAD_REQUEST
        return Response(response, status=status_code)
