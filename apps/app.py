from flask import Flask


def create_app():
    app = Flask(__name__)

    from apps.crud import views as crud_views

    app.register_blueprint(crud_views.crud, url_prefix="/crud")
    return app
