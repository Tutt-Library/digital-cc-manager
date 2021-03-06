"""Digital CC Manager Views"""

__author__ = "Jeremy Nelson, Sarah Bogard"

import requests
from flask import abort, render_template, request

from .app import app
from .forms import DeleteFedoraObjectForm, MODSMetadataForm, MODSBatchUpdateForm
from .forms import SelectPIDForm
from .models import MODS

@app.route("/batch", methods=["GET", "POST"])
def batch_operations():
    mods_form = MODSMetadataForm()
    mods_update_form = MODSBatchUpdate()
    return render_template(
        "manager/batch.html",
        obj_form=mods_form,
        update_mods=mods_update_form)



@app.route("/new", methods=["GET", "POST"])
def new_fedora_object():
    """New View for adding and saving Fedora Objects"""
    mods_form = MODSMetadataForm()
    if mods_form.validate_on_submit():
        return "Success {}".format(mods)
    return render_template(
        "manager/object.html",
        action="Add",
        obj_form=mods_form)

@app.route("/delete", methods=["GET", "POST"])
def remove_fedora_object():
    delete_form = DeleteFedoraObjectForm()
    if delete_form.validate_on_submit():
        pid = delete_form.pid
        return "Successfully deleted {}".format(pid)
    return render_template(
        "manager/delete.html",
        delete_form=delete_form)

@app.route("/update", methods=["GET", "POST"])
def update_fedora_object():
    pid = request.values.get("pid")
    if pid is None:
        return render_template(
            "manager/select.html", 
            select_pid_form = SelectPIDForm())
    mods_base_url = "{}{}/datastreams/MODS".format(
        app.config.get("REST_URL"),
        pid)
    get_mods_url = "{}/content".format(mods_base_url)
    mods_result = requests.get(
        get_mods_url,
        auth=app.config.get("FEDORA_AUTH"))
    if mods_result.status_code > 399:
        abort(500)
    mods_doc = MODS(xml=mods_result.text)
    mods_form = MODSMetadataForm()
    mods_doc.get_info(pid, app.config, mods_form)
    mods_doc.populate(mods_form)
    return render_template(
        "manager/object.html",
        action="Edit {}".format(pid),
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
