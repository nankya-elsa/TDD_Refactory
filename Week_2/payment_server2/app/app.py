# app.py — creates the flask app and wires all the routes and services together

from flask import Flask
from app.routes.customers import create_customers_routes
from app.routes.payments import create_payments_routes
from app.services.payment_service import PaymentService
from app.repos.fake_payment_repo import FakePaymentRepo

def create_app(service=None):
    # create the flask app
    app = Flask(__name__)
    
    # if no service is passed in, create a real one
    # if a mock service is passed in from a test, use that instead
    if service is None:
        repo = FakePaymentRepo()
        service = PaymentService(repo)
    
    # register all routes and hand them the service
    create_customers_routes(app, service)
    create_payments_routes(app, service)
    
    return app