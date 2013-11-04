==================
Overviews on views
==================

Options
=======

Highchart views all share the same general options:

* ``title`` (defaults as ``None``): The title of the graph
* ``subtitle`` (defaults as ``None``): will display a subtitle. May contain
  HTML tags (including links)


Basic usage
===========

Overriding options
------------------

Any option (or parameter) is a property, but it can be easily replaced by a
method if you need to generate it using code.

Examples:

.. code-block:: python

    class BarView(HighChartsBarView):
        title = 'My new (static) title'


    class BarViewAgain(HighChartsBarView):

        @property
        def title(self):
            return 'My stats for %s' % datetime.date.today()

