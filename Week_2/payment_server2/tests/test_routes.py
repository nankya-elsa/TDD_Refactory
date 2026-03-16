
# test_routes.py — tests for the HTTP routes
# the service is mocked in all tests — we only check HTTP behaviour here
# business logic is already tested in test_payment_service.py

import unittest
from unittest.mock import Mock
from app.app import create_app

class RouteTests(unittest.TestCase):

    def setUp(self):
        # create a mock service — just an actor, no real logic
        self.mock_service = Mock()
        
        # create the app and inject the mock service instead of the real one
        self.app = create_app(self.mock_service).test_client()

    def test_post_customers_returns_201_with_valid_input(self):
        # tell the mock what to return when create_customer is called
        # no real logic — just acting, handing back a fake customer
        self.mock_service.create_customer.return_value = {
            "id": "cus_1",
            "name": "Alice",
            "email": "alice@gmail.com"
        }
        
        # send a POST request to /customers with valid input
        response = self.app.post(
            '/customers',
            json={"name": "Alice", "email": "alice@gmail.com"}
        )
        
        # check the route returned 201 and the correct customer object
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertEqual(data['name'], 'Alice')
        self.assertEqual(data['email'], 'alice@gmail.com')

    def test_post_customers_returns_400_when_name_is_missing(self):
        # send a POST request with no name in the body
        response = self.app.post(
            '/customers',
            json={"email": "alice@gmail.com"}  # name is missing
        )
        
        # check the route returned 400 bad request
        self.assertEqual(response.status_code, 400)
        
        # check the service was never called — no point calling it with invalid input
        self.mock_service.create_customer.assert_not_called()

    def test_post_payments_returns_201_with_valid_input(self):
        # tell the mock what to return when create_payment is called
        self.mock_service.create_payment.return_value = {
            "id": "pay_1",
            "customer_id": "cus_1",
            "amount": 1000,
            "currency": "usd",
            "status": "pending"
        }
        
        # send a POST request to /payments with valid input
        response = self.app.post(
            '/payments',
            json={"customer_id": "cus_1", "amount": 1000, "currency": "usd"}
        )
        
        # check the route returned 201 and the correct payment object
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertEqual(data['status'], 'pending')
        self.assertEqual(data['amount'], 1000)

    def test_post_payments_returns_400_when_amount_is_missing(self):
        # send a POST request with no amount in the body
        response = self.app.post(
            '/payments',
            json={"customer_id": "cus_1", "currency": "usd"}  # amount is missing
        )
        
        # check the route returned 400 bad request
        self.assertEqual(response.status_code, 400)
        
        # check the service was never called — no point calling it with invalid input
        self.mock_service.create_payment.assert_not_called()

    def test_post_capture_returns_200_when_capture_succeeds(self):
        # tell the mock what to return when capture_payment is called
        self.mock_service.capture_payment.return_value = {
            "id": "pay_1",
            "customer_id": "cus_1",
            "amount": 1000,
            "currency": "usd",
            "status": "succeeded"  # status changed from pending to succeeded
        }
        
        # send a POST request to capture the payment
        response = self.app.post('/payments/pay_1/capture')
        
        # check the route returned 200 and the updated payment
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['status'], 'succeeded')

    def test_post_payments_amount_of_1_returns_201(self):
        # 1 is the minimum valid amount — should return 201
        self.mock_service.create_payment.return_value = {
            "id": "pay_1",
            "customer_id": "cus_1",
            "amount": 1,
            "currency": "usd",
            "status": "pending"
        }
        
        response = self.app.post(
            '/payments',
            json={"customer_id": "cus_1", "amount": 1, "currency": "usd"}
        )
        
        self.assertEqual(response.status_code, 201)

    def test_post_payments_amount_of_0_returns_400(self):
        # 0 is not a valid amount — should return 400
        self.mock_service.create_payment.side_effect = ValueError('Invalid amount')
        
        response = self.app.post(
            '/payments',
            json={"customer_id": "cus_1", "amount": 0, "currency": "usd"}
        )
        
        self.assertEqual(response.status_code, 400)

    def test_post_payments_amount_of_negative_returns_400(self):
        # negative amount is not valid — should return 400
        self.mock_service.create_payment.side_effect = ValueError('Invalid amount')
        
        response = self.app.post(
            '/payments',
            json={"customer_id": "cus_1", "amount": -1, "currency": "usd"}
        )
        
        self.assertEqual(response.status_code, 400)

    def test_get_customer_unknown_id_returns_404(self):
        # tell the mock to return None — customer doesn't exist
        self.mock_service.get_customer.return_value = None
        
        response = self.app.get('/customers/cus_999')
        
        self.assertEqual(response.status_code, 404)
        data = response.get_json()
        self.assertEqual(data['error'], 'Customer not found')

    def test_get_payment_unknown_id_returns_404(self):
        # tell the mock to return None — payment doesn't exist
        self.mock_service.get_payment.return_value = None
        
        response = self.app.get('/payments/pay_999')
        
        self.assertEqual(response.status_code, 404)
        data = response.get_json()
        self.assertEqual(data['error'], 'Payment not found')

if __name__ == "__main__":
    unittest.main()