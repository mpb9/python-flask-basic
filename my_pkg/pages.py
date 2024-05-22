from flask import Blueprint, render_template

bp = Blueprint(name="pages", import_name=__name__)


@bp.route(rule="/")
def home():
    return render_template("pages/home.html")


@bp.route(rule="/about")
def about():
    return render_template("pages/about.html")
