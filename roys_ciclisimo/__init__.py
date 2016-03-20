from datetime import datetime
import os

from flask import Flask
from flask import render_template


app = Flask(__name__)

config = {
    'endpoints': {
        'base': 'https://api.instagram.com/v1',
        'tags': {
            'info': '/tags/{hashtag}',
            'recent': '/tags/{hashtag}/media/recent',
            'search': '/tags/search',
            },
    },
    'static_dir': '%s/static' % os.path.dirname(os.path.realpath(__file__)),
}


# TODO:
#   - query for images from sqlite
#   - shuffle list of images
@app.route('/')
def index():
    context = {
        'datetime': datetime.now(),
        'images': [],
        }
    return render_template('index.html', **context)
