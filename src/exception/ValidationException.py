from flask import jsonify

from src.constant.HttpCode import HTTP_STATUS_CODE_BAD_REQUEST


class ValidationException(Exception):
    pass

    # def get_response(self):
    #     return jsonify({
    #         'Error': 'ValidationException',
    #         'Message': self.message
    #     }), HTTP_STATUS_CODE_BAD_REQUEST