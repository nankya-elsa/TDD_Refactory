
# payments.py — HTTP routes for payment endpoints
# receives requests, checks basic input, calls the service, returns responses
# business logic lives in the service layer not here

from flask import jsonify, request

def create_payments_routes(app, service):
    
    @app.post('/payments')
    def create_payment():
        # read the json body from the request
        body = request.get_json()
        
        # check that all required fields are present — if not return 400 immediately
        if not body or 'customer_id' not in body:
            return jsonify({"error": "customer_id is required"}), 400
        
        if 'amount' not in body:
            return jsonify({"error": "amount is required"}), 400
        
        if 'currency' not in body:
            return jsonify({"error": "currency is required"}), 400
        
        # call the service to create the payment
        # the service handles all the business rules
        new_payment = service.create_payment(
            body['customer_id'],
            body['amount'],
            body['currency']
        )
        
        # return the new payment with 201 created
        return jsonify(new_payment), 201
    
    @app.post('/payments/<payment_id>/capture')
    def capture_payment(payment_id):
        # call the service to capture the payment
        # the service handles the status transition from pending to succeeded
        updated_payment = service.capture_payment(payment_id)
        
        # return the updated payment with 200
        return jsonify(updated_payment), 200