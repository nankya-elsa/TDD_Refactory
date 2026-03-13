
# tests for the business logic in payment_service.py
# we inject a fake repo into the service so tests are independent of any database

import unittest
from app.services.payment_service import PaymentService
from app.repos.fake_payment_repo import FakePaymentRepo

class PaymentServiceTests(unittest.TestCase):

    def setUp(self):
        # create a fresh repo and inject it into the service before every test
        self.repo = FakePaymentRepo()
        self.service = PaymentService(self.repo)

    def test_create_customer_returns_correct_name_and_email(self):
        # create a customer and check the name and email are saved correctly
        customer = self.service.create_customer('Alice', 'alice@gmail.com')
        self.assertEqual(customer['name'], 'Alice')
        self.assertEqual(customer['email'], 'alice@gmail.com')

    def test_create_customer_raises_error_when_name_is_empty(self):
        # empty name should raise a ValueError with a clear message
        with self.assertRaises(ValueError) as context:
            self.service.create_customer('', 'alice@gmail.com')
        self.assertEqual(str(context.exception), "Name is required")

    def test_create_payment_returns_payment_with_pending_status(self):
        # first create a customer because a payment needs a customer
        customer = self.service.create_customer('Alice', 'alice@gmail.com')

        # now create a payment for that customer
        payment = self.service.create_payment(customer['id'], 1000, 'usd')

        # check the payment has the correct fields
        self.assertEqual(payment['customer_id'], customer['id'])
        self.assertEqual(payment['amount'], 1000)
        self.assertEqual(payment['currency'], 'usd')
        self.assertEqual(payment['status'], 'pending')
        self.assertTrue(payment['id'].startswith('pay_'))

    def test_create_payment_raises_error_when_amount_is_zero(self):
        # first create a customer because a payment needs a customer
        customer = self.service.create_customer('Alice', 'alice@gmail.com')

        # try to create a payment with zero amount
        with self.assertRaises(ValueError) as context:
            self.service.create_payment(customer['id'], 0, 'usd')
        self.assertEqual(str(context.exception), "Invalid amount")

    def test_capture_payment_changes_status_to_succeeded(self):
        # first create a customer because a payment needs a customer
        customer = self.service.create_customer('Alice', 'alice@gmail.com')

        # now create a payment for that customer
        payment = self.service.create_payment(customer['id'], 1000, 'usd')

        # capture the payment, status should change to succeeded
        result = self.service.capture_payment(payment['id'])

        # check the status was updated
        self.assertEqual(result['status'], 'succeeded')

    if __name__ == "__main__":
        unittest.main()