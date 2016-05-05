"""Digital CC Manager Views"""

__author__ = "Jeremy Nelson, Sarah Bogard"

from flask import abort, render_template, request

from .app import app
from .forms import DeleteFedoraObject, MODSMetadata, MODSBatchUpdate

@app.route("/batch", methods=["GET", "POST"])
def batch_operations():
    mods_form = MODSMetadata()
    mods_update_form = MODSBatchUpdate()
    return render_template(
        "manager/batch.html",
        obj_form=mods_form,
        update_mods=mods_update_form)


@app.route("/delete", methods=["GET", "POST"])
def remove_fedora_object():
    delete_form = DeleteFedoraObject()
    if delete_form.validate_on_submit():
        pid = delete_form.pid
        return "Successfully deleted {}".format(pid)
    return render_template(
        "manager/delete.html",
        delete_form=delete_form)


@app.route("/new", methods=["GET", "POST"])
def new_fedora_object():
    """New View for adding and saving Fedora Objects"""
    mods_form = MODSMetadata()
    print("Validated {}".format(mods_form.errors()))
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
