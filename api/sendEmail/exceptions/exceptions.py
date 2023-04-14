from rest_framework.exceptions import APIException


class CustomException(APIException):
    status_code = 400
    default_detail = 'A server error occurred.'
    default_code = 'server_error'
