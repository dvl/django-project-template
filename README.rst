=======================
django-project-template
=======================

This project provides an alternative startproject structure with some
boilerplate code for a quick start of your Django Projects.

************
Installation
************

.. code-block:: sh

  $ django-admin.py startproject --extension=txt,json --name=Makefile,Procfile,.env-example --template=https://github.com/dvl/django-project-template/archive/master.zip my_project
  $ cd my_project
  $ npm install
  $ cp .env-exemple .env
  $ vim .env (to edit your database settings)
  $ pip install -r requirements.txt

*********
Featuring
*********

* `django-debug-toolbar` and `django-extensions` because every project should
  have it.
* `django-flat-theme` that probably will be included in a future Django's
  release, so you can get familiar with it.
* A `settings.py` compatible with 12factor_ powered by `python-decouple`
  and `dj-database-url`.
* <strike>Custom login page based on `contrib.auth` (so maybe people will stop doing
  it from scratch).</strike> not done yet
* `bower` for assets management.
* `Procfile`, `whitenoise` and `waitress-server` for easy deployment on Heroku.
* `Makefile` to run tests and get `coverage` report.
* `bcrypt` instead of `pbkdf2` (see notes bellow).

*****
Notes
*****

This project is configured to use `bcrypt` instead of Django's default `pbkdf2`
because it's better but you may need an additional package to make it works,
to install use:

.. code-block:: sh

  $ sudo apt-get install libssl-dev libffi-dev python-dev

You can also remove `PASSWORD_HASHERS` from `settings.py` and `bcrypt==1.1.1`
from `requirements.txt` to make Django use the default `pbkdf2` and no
additional extra package will be required.


.. _12factor: http://12factor.net/
