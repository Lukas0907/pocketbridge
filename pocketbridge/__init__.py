import random
import string

from flask import Blueprint, Flask, abort, current_app, redirect, request, url_for
from flask_redis import FlaskRedis
from secrets import compare_digest


redis_client = FlaskRedis()

bp = Blueprint("pocketbridge", __name__)


def create_app():
    app = Flask(__name__)
    app.config.from_object("pocketbridge.default_settings")
    app.config.from_envvar("POCKETBRIDGE_SETTINGS")

    if not app.config["POCKETBRIDGE_SECRET"]:
        raise ValueError("Please set POCKETBRIDGE_SECRET first")

    redis_client.init_app(app)

    app.register_blueprint(bp)

    return app


@bp.route("/")
def index():
    abort(404)


@bp.get("/<id>")
def get(id):
    content = redis_client.get(id)
    if not content:
        abort(404)

    return b"<!doctype html><html><body>%s</body></html>" % content


@bp.post("/")
def share():
    try:
        content = request.form["content"]
        secret = request.form["secret"]
    except KeyError:
        abort(400)

    if not compare_digest(secret, current_app.config["POCKETBRIDGE_SECRET"]):
        abort(403)

    key = "".join(random.choice(string.ascii_lowercase) for i in range(10))
    redis_client.set(key, content, ex=current_app.config["POCKETBRIDGE_EXPIRE"])

    return redirect(url_for(".get", id=key))
