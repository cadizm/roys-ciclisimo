import shutil

import requests
import wget

from roys_ciclisimo import config, secrets


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


# TODO:
#   - skip downloading media that has already been downloaded
#   - save image metadata and path on disk to sqlite?
def get_media(hashtag):
    for res in _get_metadata(hashtag):
        if res['meta']['code'] != 200:
            continue

        for media in res['data']:
            caption = media.get('caption', {})
            caption = caption.get('text', '')

            for resolution, image in media['images'].iteritems():
                try:
                    filename = wget.download(image['url'])
                    dest = '%s/images/%s' % (config['static_dir'], resolution)
                    shutil.move(filename, dest)

                except shutil.Error:
                    import os
                    os.remove(filename)


if __name__ == '__main__':
    get_media(hashtag='roysciclisimocrew')
