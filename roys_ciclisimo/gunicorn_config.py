
# http://docs.gunicorn.org/en/latest/settings.html

chdir = '/opt/cadizm/lib/roys-ciclisimo/roys_ciclisimo'

bind = '127.0.0.1:5003'
proc_name = 'roysciclisimo.wsgi'
pidfile = '/opt/cadizm/var/run/roysciclisimo.pid'

import multiprocessing
workers = multiprocessing.cpu_count() * 2 + 1

reload = True
daemon = False  # use systemd
capture_output = True

user = 'www-data'
group = 'www-data'

accesslog = '/opt/cadizm/var/log/roysciclisimo-access.log'
errorlog = '/opt/cadizm/var/log/roysciclisimo-error.log'
