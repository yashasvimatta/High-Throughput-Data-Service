from constant.FieldNames import USER_ID_FIELD_NAME, USER_NAME_FIELD_NAME
from exception.validation_exception import ValidationException


class CreateUserRequestValidator:

    @classmethod
    def validate(cls, request):
        payload = request.get_json()

        if USER_ID_FIELD_NAME not in payload:
            raise ValidationException("user_id not present in request")
        
        if USER_NAME_FIELD_NAME not in payload:
            raise ValidationException("user_name not present in request")        
