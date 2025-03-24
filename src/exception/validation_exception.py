from response.api_responses import APIResponse


class ValidationException(Exception):
    def get_api_response(self):
        return APIResponse.bad_request(self, 'ValidationException')
