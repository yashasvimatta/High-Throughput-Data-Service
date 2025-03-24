from flask import jsonify
from multipledispatch import dispatch

from constant.HttpCode import HTTP_STATUS_CODE_NOT_FOUND, HTTP_STATUS_CODE_OK, HTTP_STATUS_CODE_CREATED, \
    HTTP_STATUS_CODE_CONFLICT, HTTP_STATUS_CODE_BAD_REQUEST, HTTP_STATUS_CODE_INTERNAL_SERVER_ERROR


class APIResponse:

    @classmethod
    @dispatch(type, object)
    def ok_success(cls, return_object):
        return jsonify(return_object), HTTP_STATUS_CODE_OK

    @classmethod
    @dispatch(type, str)
    def ok_success(cls, message):
        return jsonify({
            'Message': message
        }), HTTP_STATUS_CODE_OK

    @classmethod
    def created(cls, message):
        return jsonify({"Message": message}), HTTP_STATUS_CODE_CREATED

    @classmethod
    def bad_request(cls, message, error_type):
        return jsonify({
            'ErrorType': error_type,
            'Message': message
        }), HTTP_STATUS_CODE_BAD_REQUEST

    @classmethod
    def not_found(cls, message):
        return jsonify({
            'ErrorType': 'RecordNotFoundException',
            'Message': message
        }), HTTP_STATUS_CODE_NOT_FOUND

    @classmethod
    def conflict(cls, message, error_type):
        return jsonify({
            'ErrorType': error_type,
            'Message': message
        }), HTTP_STATUS_CODE_CONFLICT

    @classmethod
    def internal_server_error(cls, message):
        return jsonify({
            'Message': message
        }), HTTP_STATUS_CODE_INTERNAL_SERVER_ERROR


