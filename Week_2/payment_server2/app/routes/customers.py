# customers.py — HTTP routes for customer endpoints
# receives requests, checks basic input, calls the service, returns responses
# business logic lives in the service layer not here

from flask import Flask, jsonify, request

def create_customers_routes(app, service):
    
    @app.post('/customers')
    def create_customer():
        # read the json body from the request
        body = request.get_json()

        # check that name is present in the body — if not return 400 immediately
        # we don't call the service with invalid input
        if not body or 'name' not in body:
            return jsonify({"error": "name is required"}), 400
        
        # check that email is present in the body — if not return 400 immediately
        if 'email' not in body:
            return jsonify({"error": "email is required"}), 400
        
        # call the service to create the customer
        # the service handles all the business rules
        new_customer = service.create_customer(body['name'], body['email'])
        
        # return the new customer with 201 created
        return jsonify(new_customer), 201