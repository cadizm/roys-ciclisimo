from contextlib import contextmanager
import random

from sqlalchemy import create_engine

from roys_ciclisimo.config import config


engine = create_engine(config['conn_str'])


@contextmanager
def _get_images():
    conn = engine.connect()
    yield conn.execute('select * from images')
    conn.close()


def get_images():
    res = []
    with _get_images() as images:
        res = [i for i in images]
    random.shuffle(res)

    return res


def save_image(id_, path, caption):
    caption = caption.replace('"', '""')  # escape
    vals = ('id', 'standard_resolution', 'caption', id_, path, caption)
    stmt = 'insert into images (%s, %s, %s) values ("%s", "%s", "%s")' % vals

    conn = engine.connect()
    conn.execute(stmt)
    conn.close()


def get_image_ids():
    conn = engine.connect()
    res = [r for r in
        conn.execute('select id from images')]
    conn.close()

    return res
