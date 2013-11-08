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

The view
--------

.. code-block:: python

    from highcharts.views import HighChartsBarView

    class BarView(HighChartsBarView):
        categories = ['Orange', 'Bananas', 'Apples']

        @property
        def series(self):
            result = []
            for name in ('Joe', 'Jack', 'William', 'Averell'):
                data = []
                for x in range(len(self.categories)):
                    data.append(random.randint(0, 10))
                result.append({'name': name, "data": data})
            return result

The template
------------

.. code-block:: django

    {% load staticfiles %}<!doctype html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Hello</title>
        <script type="text/javascript" src="//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
        <script type="text/javascript" src="{% static 'js/highcharts/highcharts.js' %}"></script>
        <script type="text/javascript">
        $(function () {
            $.getJSON("{% url 'bar' %}", function(data) {
                $('#container').highcharts(data);
            });
        });
        </script>
    </head>
    <body>
    <div id="container" style="height: 300px"></div>
    </body>
    </html>

.. warning::

    Please note that the highcharts.js file should be called **after** the
    JQuery library.

Available views
===============

.. toctree::
    :maxdepth: 2
    :glob:

    views/*

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

