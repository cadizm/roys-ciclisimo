from datetime import datetime

from flask import render_template

from roys_ciclisimo.db import get_images


def index():
    context = {
        'datetime': datetime.now(),
        'images': get_images(),
        }

    return render_template('index.html', **context)
