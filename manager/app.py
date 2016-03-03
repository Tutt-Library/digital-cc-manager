__author__ = "Jeremy Nelson, Sarah Bogard"

from flask import Flask

app = Flask(__name__,  instance_relative_config=True)
app.config.from_pyfile('conf.py')

from .views import *
from .filters import *
