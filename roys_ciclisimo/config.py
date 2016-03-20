import os


_dir = os.path.dirname(os.path.realpath(__file__))

config = {
    'endpoints': {
        'base': 'https://api.instagram.com/v1',
        'tags': {
            'info': '/tags/{hashtag}',
            'recent': '/tags/{hashtag}/media/recent',
            'search': '/tags/search',
            },
    },
    'base_dir': '%s' % _dir,
    'static_dir': '%s/static' % _dir,
    'conn_str': 'sqlite:///%s/roys.db' % _dir,
}
