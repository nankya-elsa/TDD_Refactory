from flask import Flask, json

def create_app():
    app = Flask(__name__)

    @app.route('/hello')
    def hello():
        return json.dumps({'message': 'Hello, World!'})

    return app