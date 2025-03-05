import unittest
from unittest.mock import Mock

from src.exception import ValidationException
from src.validator import CreateUserRequestValidator

class Test_CreateUserRequestValidator(unittest.TestCase):
    def test_invalid_request_user_id_not_present(self):
        
        mock_request = Mock()
        mock_request.get_json.return_value = {
            'user_name': 'Some name'
        }

        with self.assertRaises(ValidationException) as ve:
            CreateUserRequestValidator.validate(mock_request)
        
if __name__ == '__main__':
    unittest.main()
