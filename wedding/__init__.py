import sys, os
from flask import Flask

app = Flask(__name__.split('.')[0])

import wedding.views
