import unittest
from src.create_app import create_app

class PaymentServerTests(unittest.TestCase): # class to contain all our tests
    def setUp(self):
        self.app = create_app().test_client() # create an instance of our app
        

    def  test_create_customer_returns_201(self):
        # POST to / customers with a name and email should return 201, created
        response = self.app.post('/customers', json={'name': 'Alice', 'email': 'alice@gmail.com'})
        self.assertEqual(response.status_code, 201)

    def test_create_customer_returns_correct_data(self):
        # POST a new customer and check the response body has the right fields
        response = self.app.post('/customers', json={"name": "Alice", "email": "alice@gmail.com"})
        data = response.get_json()

        # check the name and email match what we sent
        self.assertEqual(data['name'], 'Alice')
        self.assertEqual(data['email'], 'alice@gmail.com')

        # check that an id was generated and not empty
        self.assertIsNotNone(data['id'])

        # check that the id starts with "cus_"
        self.assertTrue(data['id'].startswith('cus_'))

    def test_get_customer_by_id_returns_200(self):
        # create a new customer so we have something to fetch
        create_response = self.app.post('/customers', json={"name": "Alice", "email": "alice@gmail.com"})

        # grab the id from the created customer
        customer_id = create_response.get_json()['id']

        # now get that customer using their id
        response = self.app.get(f'/customers/{customer_id}')
        data = response.get_json()

        # check we got a 200 back
        self.assertEqual(response.status_code, 200)

        # check the data matches what we created
        self.assertEqual(data['id'], customer_id)
        self.assertEqual(data['name'], 'Alice')
        self.assertEqual(data['email'], 'alice@gmail.com')

    # PAYMENTS
    def test_create_payment_returns_201(self):
        # first create a customer because a payment needs to be associated with a customer
        create_response = self.app.post('/customers', json={"name": "Alice", "email": "alice@gmail.com"})
        customer_id = create_response.get_json()['id']

        # now create a payment for that customer
        response = self.app.post('/payments', json={"customer_id": customer_id, "amount": 1000, "currency": "usd"})

        # check we got a 201 back
        self.assertEqual(response.status_code, 201)

    def test_create_payment_returns_correct_data(self):
        # first create a customer because a payment needs to be associated with a customer
        create_response = self.app.post('/customers', json={"name": "Alice", "email": "alice@gmail.com"})
        customer_id = create_response.get_json()['id']

        # now create a payment for that customer
        response = self.app.post('/payments', json={"customer_id": customer_id, "amount": 1000, "currency": "usd"})
        data = response.get_json()

        # check the data matches what we sent
        self.assertEqual(data['customer_id'], customer_id)
        self.assertEqual(data['amount'], 1000)
        self.assertEqual(data['currency'], "usd")
        self.assertEqual(data['status'], "pending")
        self.assertIsNotNone(data['id'])
        self.assertTrue(data['id'].startswith('pay_'))

    def test_update_payment_status_returns_200(self):
        # first create a customer because a payment needs to be associated with a customer
        create_response = self.app.post('/customers', json={"name": "Alice", "email": "alice@gmail.com"})
        customer_id = create_response.get_json()['id']

        # now create a payment for that customer
        payment_response = self.app.post('/payments', json={"customer_id": customer_id, "amount": 1000, "currency": "usd"})
        payment_id = payment_response.get_json()['id']

        # now update the payment status to "succeeded"
        update_response = self.app.patch(f'/payments/{payment_id}', json={"status": "succeeded"})
        data = update_response.get_json()

        # check we got a 200 back
        self.assertEqual(update_response.status_code, 200)

        # check the status was updated
        self.assertEqual(data['status'], "succeeded")

    # REFUNDS
    def test_create_refund_returns_201(self):
        # first create a customer because a payment needs to be associated with a customer
        create_response = self.app.post('/customers', json={"name": "Alice", "email": "alice@gmail.com"})
        customer_id = create_response.get_json()['id']

        # create a payment for that customer
        payment_response = self.app.post('/payments', json={"customer_id": customer_id, "amount": 1000, "currency": "usd"})
        payment_id = payment_response.get_json()['id']

        # a refund can only be created for a payment that has succeeded, so we update the payment status to "succeeded"
        self.app.patch(f'/payments/{payment_id}', json={"status": "succeeded"})

        # create a refund for that payment
        refund_response = self.app.post('/refunds', json={"payment_id": payment_id, "amount": 500})
        data = refund_response.get_json()

        # check we got a 201 back
        self.assertEqual(refund_response.status_code, 201)

    def test_refund_amount_cannot_exceed_payment_amount(self):
        # first create a customer
        create_customer_response = self.app.post(
            '/customers',
            json={"name": "Alice", "email": "alice@gmail.com"}
        )
        customer_id = create_customer_response.get_json()['id']

        # then create a payment for that customer with amount 1000
        create_payment_response = self.app.post(
            '/payments',
            json={"customer_id": customer_id, "amount": 1000, "currency": "usd"}
        )
        payment_id = create_payment_response.get_json()['id']

        # update the payment status to succeeded before refunding
        self.app.patch(
            f'/payments/{payment_id}',
            json={"status": "succeeded"}
        )

        # try to refund 2000 which is more than the original payment of 1000
        response = self.app.post(
            '/refunds',
            json={"payment_id": payment_id, "amount": 2000}
        )

        # this should be rejected with a 400
        self.assertEqual(response.status_code, 400)

    # def test_create_payment(self):
    #     #create a customer
    #     response = self.app.post('/customers', json={"name": "Alice", "email": "alice@gmail.com"})
    #     customer_id  = response.get_json()['id']
    #     # create payment for the customer
    #     new_response = self.app.post('/payments', json={{"customer_id": customer_id, "amount": 1000, "currency": "usd"}})
    #     self.assertEqual(new_response.status_code, 201)

if __name__ == '__main__':
    unittest.main()