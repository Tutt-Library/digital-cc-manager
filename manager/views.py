"""Digital CC Manager Views"""

__author__ = "Jeremy Nelson, Sarah Bogard"

from flask import abort, render_template, request

from .app import app
from .forms import MODSMetadata

@app.route("/new", methods=["GET", "POST"])
def new_fedora_object():
    """New View for adding and saving Fedora Objects"""
    mods_form = MODSMetadata()
    if mods_form.validate_on_submit():
        return "Success"
    return render_template(
        "manager/object.html",
        action="Add",
        obj_form=mods_form)


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
