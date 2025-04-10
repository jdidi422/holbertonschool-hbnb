from flask import Flask
from flask_restx import Api

def create_app():
    app = Flask(__name__)
    api = Api(app)

    # Import après la création de l'API
    from app.api.v1.reviews import api as reviews_ns
    api.add_namespace(reviews_ns, path='/reviews')

    return app
