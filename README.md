
Setup
=====

```
$ mkvirtualenv roys
$ pip install -r requirements/base.txt
$ sqlite3 roys_ciclisimo/roys.db < bin/schema.sql
$ python bin/rcc.py
$ python bin/runserver.py
```
