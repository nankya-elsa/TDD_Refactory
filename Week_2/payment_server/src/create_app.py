from flask import Flask, jsonify, request
import time

def create_app():
    # create the flask pp
    app = Flask(__name__)

    # in-memory storage, our fake database
    customers = []
    payments = []
    refunds = []

    @app.post('/customers')
    def create_customer():
        #read the json body from the request
        body = request.get_json()

        # build a new customer object
        new_customer = {
            "id": "cus_" + str(int(time.time() * 100)),
            "name": body['name'],
            "email": body['email']
        }
        # add the new customer to our in-memory list
        customers.append(new_customer)

        # return the new customer with a 201 status code
        return jsonify(new_customer), 201
    
    @app.get('/customers/<id>')
    def get_customer_by_id(id):
        # loop through our customers and find the one with the matching id
        for customer in customers:
            if customer['id'] == id:
                return jsonify(customer), 200
        
        # if we didn't find a customer, return a 404
        return jsonify({"error": "Customer not found"}), 404
    
    # PAYMENTS
    @app.post('/payments')
    def create_payment():
        # read the json body from the request
        body = request.get_json()
        
        # build a new payment object
        new_payment = {
            "id": "pay_" + str(int(time.time() * 100)),
            "customer_id": body['customer_id'],
            "amount": body['amount'],
            "currency": body['currency'],
            "status": "pending"
        }
        # add the new payment to our in-memory list
        payments.append(new_payment)

        # return the new payment with a 201 status code
        return jsonify(new_payment), 201
    
    @app.patch('/payments/<id>')
    def update_payment_status(id):
        # read the json body from the request
        body = request.get_json()

        # loop through our payments and find the one with the matching id
        for payment in payments:
            if payment['id'] == id:
                # update the payment status
                payment['status'] = body['status']
                return jsonify(payment), 200
        
        # if we didn't find a payment, return a 404
        return jsonify({"error": "Payment not found"}), 404
    
    @app.post('/refunds')
    def create_refund():
        # read the json body from the request
        body = request.get_json()
        
        #find the payment thi refund is for
        for payment in payments:
            if payment['id'] == body['payment_id']:

                # check refund amount doesnot exceed the original payment amount
                if body['amount'] > payment['amount']:
                    return jsonify({"error": "Refund amount cannot exceed payment amount"}), 400
                
                # build a new refund object
                new_refund = {
                    "id": "ref_" + str(int(time.time() * 100)),
                    "payment_id": body['payment_id'],
                    "amount": body['amount'],
                    "status": "succeeded"
                }
                # add the new refund to our in-memory list
                refunds.append(new_refund)

                # return the new refund with a 201 status code
                return jsonify(new_refund), 201
        
        # if we didn't find a payment, return a 404
        return jsonify({"error": "Payment not found"}), 404


    # @app.post('/payments')
    # def create_payment():
    #     body = request.get_json()
    #     new_payment ={
    #         "cutomer_id": body['customer_id'],
    #         "amount": body['amount'],
    #         "currency": body['currency'],
    #     }

    #     payments.append(new_payment)
    #     return jsonify(new_payment),201
    
    #return the finished app
    return app