"""Digital CC Manager Views"""

__author__ = "Jeremy Nelson, Sarah Bogard"

from flask import render_template

from .app import app

@app.route("/<path:page>")
@app.route("/")
def index(page=None):
    """Index route displays default page for application

    Args:
        page:  Path to page, default is None
    """
    if page is None:
        return render_template("manager/index.html")
    return "Page is {}".format(page)
