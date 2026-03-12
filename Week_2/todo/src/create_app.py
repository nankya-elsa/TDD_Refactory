from flask import Flask, jsonify, request

todos = []

def create_app():
    app = Flask(__name__)

    @app.get('/todos')
    def get_todos():
        return jsonify(todos), 200

    

    return app