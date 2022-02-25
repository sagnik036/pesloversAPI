from rest_framework import serializers


class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField(
        required=True,
        max_length=None,
        allow_empty_file=False,
        help_text="""
            Upload files. Can be anything.
            Please use front end restriction for Images.
            Maximum file size is 5MB.
        """,
        # use_url=UPLOADED_FILES_USE_URL
    )
    path = serializers.CharField(
        max_length=250,
        required=False,
        help_text='''
            It is actually directory. Where you want to save.
            For example, if you want to upload profile picture,
            use 'profile_pictures/username'.
            Default is 'documents'.
        '''
    )

    @classmethod
    def validate(cls, data):
        errors = {}
        max_upload_size = 5242880
        file = data.get("file")
        file_size = file.size

        if int(file_size) > max_upload_size:
            errors["file"] = "Too large file. Maximum 5MB is supported."

        if errors:
            raise serializers.ValidationError(errors)
        return super(FileUploadSerializer, cls).validate(cls, data)
