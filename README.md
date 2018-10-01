tilehuria-server
===

Server for running [TileHuria](https://github.com/ivangayton/tilehuria).


Tools for development
---

### Initial setup


```
pip install -Ur requirements.txt
```


### Running locally

To run on localhost:
```commandline
virtualenv venv
export FLASK_APP=tilehuriaserver.py
python tilehuriaserver.py
```

Additional Resources:
- [Tutorial on wsgi](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uwsgi-and-nginx-on-ubuntu-14-04)
