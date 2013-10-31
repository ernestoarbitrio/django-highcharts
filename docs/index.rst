=================
Django Highcharts
=================

Django Highchart will make it easier for you to display highcharts graphs.

Quickstart
==========

Install django-highcharts using pip (we do recommend to do it in a virtualenv).

.. code-block:: sh

    git clone https://github.com/novapost/django-highcharts.git
    cd django-highcharts
    pip install -e ./

To integrate it into a Django project, simply add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = [
        # some interesting stuff...
        'highcharts',
        # some other stuff...
    ]

Don't forget to set your `STATIC_ROOT` path and to run the following command to
update the static files:

.. code-block:: sh

    python manage.py collectstatic

You're now ready to use the available views.

.. toctree::
    :maxdepth: 2

    bar

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

