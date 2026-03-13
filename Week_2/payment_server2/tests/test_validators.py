# tests for the validator helper functions in utils/validators.py

import unittest
from app.utils.validators import validate_amount, validate_currency, validate_email

class ValidatorTests(unittest.TestCase):

    def test_validate_amount_returns_true_for_valid_amount(self):
        # 100 is a valid positive integer — should return True
        result = validate_amount(100)
        self.assertTrue(result)

    def test_validate_amount_returns_falsefor_zero(self):
        # 0 is not greater than 0 — should return False
        result = validate_amount(0)
        self.assertFalse(result)

    def test_validate_amount_returns_false_for_decimal(self):
        # 2.99 is a decimal, not a valid amount, should return Falsa
        result = validate_amount(2.99)
        self.assertFalse(result)

    def test_validate_amount_returns_false_for_negative(self):
        # -50 is negative, not a valid amount, should return False
        result = validate_amount(-50)
        self.assertFalse(result)

    def test_validate_currency_returns_true_for_valid_currency(self):
        # 'usd' is a eactly 3 characters, should return True
        result = validate_currency('usd')
        self.assertTrue(result)

    def test_validate_email_returns_true_for_valid_email(self):
       # alice@gmail.com contains @ and . should return True
       result = validate_email('alice@gmail.com')
       self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()