import unittest
from unittest.mock import Mock

from src.exception.validation_exception import ValidationException
from src.validator.create_user_request_validator import CreateUserRequestValidator

class TestCreateUserRequestValidator(unittest.TestCase):
    def test_invalid_request_user_id_not_present(self):
        mock_request = Mock()
        mock_request.get_json.return_value = {
            'user_name': 'Some name'
        }

        with self.assertRaises(ValidationException) as ve:
            CreateUserRequestValidator.validate(mock_request)

        self.assertEqual(str(ve.exception), 'user_id not present in request')

    def test_invalid_request_user_name_not_present(self):
        mock_request = Mock()
        mock_request.get_json.return_value = {
            'user_id': 100
        }

        with self.assertRaises(ValidationException) as ve:
            CreateUserRequestValidator.validate(mock_request)

        self.assertEqual(str(ve.exception), 'user_name not present in request')

        
if __name__ == '__main__':
    unittest.main()
