import logging
import shutil

import requests
import wget

from roys_ciclisimo import secrets
from roys_ciclisimo.config import config
from roys_ciclisimo.models import save_image, get_image_ids

logger = logging.getLogger(__name__)


def _hashtag_url(hashtag):
    base = config['endpoints']['base']
    recent = config['endpoints']['tags']['recent']
    url = '%s%s?access_token=%s' % (base, recent, secrets.IG_ACCESS_TOKEN)

    return url.format(hashtag=hashtag)


def _get_metadata(hashtag):
    response = requests.get(_hashtag_url(hashtag))

    while True:
        if not response.ok:
            raise Exception(response.reason)

        meta = response.json()
        yield meta

        try:
            url = meta['pagination']['next_url']
            response = requests.get(url)

        except KeyError:
            break


def get_media(hashtag):
    ids = get_image_ids()

    for res in _get_metadata(hashtag):
        if res['meta']['code'] != 200:
            continue

        for media in res['data']:
            if media['id'] in ids:
                logger.info('%s already saved' % media['id'])
                continue

            caption = media.get('caption', {})
            caption = caption.get('text', '')

            for resolution, image in media['images'].iteritems():
                if resolution == 'standard_resolution':
                    try:
                        logger.info('downloading %s' % image['url'])
                        filename = wget.download(image['url'])
                        dest = '%s/images/%s' % (config['static_dir'], resolution)
                        shutil.move(filename, dest)
                        save_image(media['id'], filename, caption)

                    except shutil.Error:
                        import os
                        os.remove(filename)


if __name__ == '__main__':
    get_media(hashtag='roysciclisimocrew')
