# fake in-memory database for testing
# stores customers, payments and refunds in dictionaries
# used instead of a real database during tests

class FakePaymentRepo:

    def __init__(self):
        # dictionaries to store our data, key is always the id
        self.customers = {}
        self.payments = {}

    def save_customer(self, customer):
        # store the customer in the dictionary using its id as the key
        self.customers[customer['id']] = customer
        return customer

    def find_customer_by_id(self, customer_id):
        # look up the customer by id — return None if not found
        return self.customers.get(customer_id, None)
    
    def find_customer_by_email(self, email):
        # loop through all customers and find the one with matching email
        for customer in self.customers.values():
            if customer['email'] == email:
                return customer
        
        # if we get here no customer was found — return None
        return None

    def save_payment(self, payment):
        # store the payment in the payments dictionary,its id as the key
        self.payments[payment['id']] = payment
        return payment

    def find_payment_by_id(self, payment_id):
        # look up the payment in the payments dictionary by id and return it
        return self.payments.get(payment_id, None)

    def clear(self):
        # helper method to clear the repo between tests
        self.customers = {}
        self.payments = {}
    