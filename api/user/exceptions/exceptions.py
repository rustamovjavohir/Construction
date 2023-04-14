from rest_framework.exceptions import APIException


class UserDoesNotExist(APIException):
    status_code = 404
    default_detail = 'User does not exist.'
    default_code = 'user_does_not_exist'

    def __init__(self, detail=None, code=None):
        if detail is None:
            detail = self.default_detail

        if code is None:
            code = self.default_code

        self.detail = detail
        self.code = code
