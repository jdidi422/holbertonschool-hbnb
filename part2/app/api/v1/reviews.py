def get_reviews_api():
    from flask_restx import Namespace
    return Namespace('reviews', description='Reviews related operations')

api = get_reviews_api()
