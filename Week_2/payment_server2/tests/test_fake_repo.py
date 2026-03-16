# tests for the fake in-memory database
# proves that the repo correctly stores and retrieves customers and payments

import unittest
from app.repos.fake_payment_repo import FakePaymentRepo

class FakeRepoTests(unittest.TestCase):

    def setUp(self):
        # create a fresh repo before every test
        self.repo = FakePaymentRepo()

    def test_save_customer_stores_and_find_customer_by_id_returns_it(self):
        # create a sample customer
        customer = {"id": "cus_1", "name": "Alice", "email": "alice@gmail.com"}
        
        # save it to the repo
        self.repo.save_customer(customer)
        
        # fetch it back using the id
        result = self.repo.find_customer_by_id("cus_1")
        
        # check it's the same customer we saved
        self.assertEqual(result['id'], 'cus_1')
        self.assertEqual(result['name'], 'Alice')
        self.assertEqual(result['email'], 'alice@gmail.com')

    def test_find_customer_by_id_returns_none_for_unknown_id(self):
        # try to fetch a customer that was never saved
        result = self.repo.find_customer_by_id('cus_999')
        
        # should return None — not an error, just nothing found
        self.assertIsNone(result)

    def test_save_payment_stores_and_find_payment_by_id_returns_it(self):
        # create a sample payment
        payment = {"id": "pay_1", "customer_id": "cus_1", "amount": 1000, "currency": "usd", "status": "pending"}
        
        # save it to the repo
        self.repo.save_payment(payment)
        
        # fetch it back using the id
        result = self.repo.find_payment_by_id("pay_1")
        
        # check it's the same payment we saved
        self.assertEqual(result['id'], 'pay_1')
        self.assertEqual(result['amount'], 1000)
        self.assertEqual(result['status'], 'pending')

    def test_find_customer_by_email_returns_customer_when_email_matches(self):
        # create and save a customer
        customer = {"id": "cus_1", "name": "Alice", "email": "alice@gmail.com"}
        self.repo.save_customer(customer)
        
        # fetch the customer using their email
        result = self.repo.find_customer_by_email("alice@gmail.com")
        
        # check it's the same customer we saved
        self.assertEqual(result['id'], 'cus_1')
        self.assertEqual(result['email'], 'alice@gmail.com')

    def test_clear_empties_all_stored_data(self):
        # save a customer and a payment
        customer = {"id": "cus_1", "name": "Alice", "email": "alice@gmail.com"}
        payment = {"id": "pay_1", "customer_id": "cus_1", "amount": 1000, "currency": "usd", "status": "pending"}
        self.repo.save_customer(customer)
        self.repo.save_payment(payment)
        
        # clear everything
        self.repo.clear()
        
        # check both are gone
        self.assertIsNone(self.repo.find_customer_by_id("cus_1"))
        self.assertIsNone(self.repo.find_payment_by_id("pay_1"))

if __name__ == "__main__":
    unittest.main()