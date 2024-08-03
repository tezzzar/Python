from flask import Flask
from payroll import pages

def create_app():
    app = Flask(__name__)
    app.register_blueprint(pages.bp)

    # @app.route('/hello')
    # def hello():
    #     return "Hello Flask!"

    return app