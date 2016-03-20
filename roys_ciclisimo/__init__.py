from flask import Flask

from roys_ciclisimo import views


app = Flask(__name__)
app.add_url_rule('/', view_func=views.index)
