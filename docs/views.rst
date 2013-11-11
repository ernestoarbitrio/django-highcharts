=====
Views
=====

Common options
==============

Highchart views all share the same general options. If one of these options
is not set by a class property or an instance property, it'll use the
default value (generally ``None``)

* ``title``: The title of the graph
* ``subtitle``: will display a subtitle. May contain
  HTML tags (including links)
* ``tooltip_point_format``: formatting the tooltip over a data point using the
  Highchart appropriate format. (e.g.: ``"{series.name} produced <b>{point.y:,.0f}</b><br/>warheads in {point.x}"``)
* ``plot_options`` (defaults to ``{}``): this dictionary will be directly
  converted into a JSON object and assigned to the data.plotOptions property on
  the client-side (it was too difficult to cover all the cases implied by this
  dictionary.)

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

Available views
===============

HighChartsBarView
-----------------

::

    from highcharts.views import HighChartsBarView


Extra options
#############

* ``categories`` (defaults to ``[]``): should return a list of string,
* ``y_axis_title`` (defaults to ``""``): the title of the Y axis.


HighChartsLineView
------------------

::

    from highcharts.views import HighChartsLineView


Extra options
#############

* ``categories`` (defaults to ``[]``): should return a list of string,
* ``y_axis_title`` (defaults to ``""``): the title of the Y axis.


HighChartsAreaView
------------------

::

    from highcharts.views import HighChartsAreaView


Extra options
#############

No extra options for the Area View (yet).
