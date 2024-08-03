from flask import Flask
from payroll import pages, database, staff, auth, books
import os

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, 'payroll.db')
    )
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    database.init_app(app)

    app.register_blueprint(pages.bp)
    app.register_blueprint(staff.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(books.bp)
    return app