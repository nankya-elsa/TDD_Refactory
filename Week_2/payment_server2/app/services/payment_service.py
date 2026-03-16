# business logic layer for the payment server
# handles all rules around customers, payments and refunds
# talks to the repository to save and fetch data

import time
from app.utils.validators import validate_amount
class PaymentService:
    def __init__(self, repo):
        # repo is injected in, so we can swap in a fake repo during tests
        self.repo = repo

    def create_customer(self, name, email):
        # check that name is not wmpty or just whitespace
        if not name or not name.strip():
            raise ValueError("Name is required")
        
        # build a new customer object
        new_customer = {
            "id": "cus_" + str(int(time.time() * 100)),
            "name": name,
            "email": email
        }
        # save the new customer to the repo
        self.repo.save_customer(new_customer)
        return new_customer


    def create_payment(self, customer_id, amount, currency):
        # check that amount is a valid positive integer using our validator function
        if not validate_amount(amount):
            raise ValueError("Invalid amount")
        
        # build a new payment object
        new_payment = {
            "id": "pay_" + str(int(time.time() * 100)),
            "customer_id": customer_id,
            "amount": amount,
            "currency": currency,
            "status": "pending"
        }
        # save the new payment to the repo
        self.repo.save_payment(new_payment)
        return new_payment

    def capture_payment(self, payment_id):
        # fetch the payment from the repo using payment_id
        payment = self.repo.find_payment_by_id(payment_id)
        # update the payment status to succeeded
        payment['status'] = 'succeeded'
        # save the updated payment to the repo
        self.repo.save_payment(payment)
        return payment