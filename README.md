## Django Highcharts

This is a Fork of novapost package to
generate charts in your Django application using Highcharts helpers.

- Pie with drilldown charts
- 3D Pie Options
- Speedometer charts
- Multiple Axes charts
- Area charts
- Bar charts
- Heatmap charts
- Polar Spider web charts
- HighStock basic charts

* `Source code is on Github <https://github.com/ernestoarbitrio/django-highcharts>`_

### Install
There are a few different ways you can install pyechonest:

* Use setuptools: `pip install git+https://github.com/ernestoarbitrio/django-highcharts.git`
* Download the zipfile from the [downloads](https://github.com/ernestoarbitrio/django-highcharts/archive/master.zip) page and install it. 
* Checkout the source: `git@github.com:ernestoarbitrio/django-highcharts.git` and install it yourself.

In your settings file:
```
INSTALLED_APPS = [
   ### other apps ###
   'highcharts'
   ### other apps ###
]
```

Don’t forget to set your STATIC_ROOT path and to run the following command to update the static files:

`python manage.py collectstatic`

Write a graph with different series type (in view.py file or if you want in a graph.py file):
```
from highcharts.views import (HighChartsMultiAxesView, HighChartsPieView,
                              HighChartsSpeedometerView, HighChartsHeatMapView, HighChartsPolarView)
                              
class BarView(HighChartsMultiAxesView):
    title = 'Example Bar Chart'
    subtitle = 'my subtitle'
    categories = ['Orange', 'Bananas', 'Apples']
    chart_type = ''
    chart = {'zoomType': 'xy'}
    tooltip = {'shared': 'true'}
    legend = {'layout': 'horizontal', 'align': 'left',
              'floating': 'true', 'verticalAlign': 'top',
              'y': -10, 'borderColor': '#e3e3e3'}

    @property
    def yaxis(self):
        y_axis = [
            {'labels': {'format': '{value} pz/sc ', 'style': {'color': '#f67d0a'}},
             'title': {'text': "Oranges", 'style': {'color': '#f67d0a'}},
             'opposite': 'true'},
            {'gridLineWidth': 1,
             'title': {'text': "Bananas", 'style': {'color': '#3771c8'}},
             'labels': {'style': {'color': '#3771c8'}, 'format': '{value} euro'}},
            {'gridLineWidth': 1,
             'title': {'text': "Apples", 'style': {'color': '#666666'}},
             'labels': {'format': '{value} pz', 'style': {'color': '#666666'}},
             'opposite': 'true'}
        ]
        return y_axis

    @property
    def series(self):
        series = [
            {
                'name': 'Orange',
                'type': 'column',
                'yAxis': 1,
                'data': [90,44,55,67,4,5,6,3,2,45,2,3,2,45,5],
                'tooltip': "{ valueSuffix: ' euro' }",
                'color': '#3771c8'
            },
            {
                'name': 'Bananas',
                'type': 'spline',
                'yAxis': 2,
                'data': [12,34,34,34, 5,34,3,45,2,3,2,4,4,1,23],
                'marker': { 'enabled': 'true' },
                'dashStyle': 'shortdot',
                'color': '#666666',
                },
            {
                'name': 'Apples',
                'type': 'spline',
                'data': [12,23,23,23,21,4,4,76,3,66,6,4,5,2,3],
                'color': '#f67d0a'
            }
        ]
        return series
```
if you want you can write a graph based on a particular class of chart. For exampla if you need a pie chart with drilldown interaction:
```
from highcharts.views import (HighChartsMultiAxesView, HighChartsPieView,
                              HighChartsSpeedometerView, HighChartsHeatMapView, HighChartsPolarView)

class PieDrilldown(HighChartsPieView):
    title = 'Torta'
    subtitle = 'torino'

    @property
    def series(self):
        series = [
            {
                'name': 'Classi',
                'colorByPoint': 'true',
                'data': [
                    {'name': 'Emorroidi',
                     'y': 10,
                     'drilldown': 'emorroidi'},
                    {'name': 'Igiene e bellezza',
                     'y': 12,
                     'drilldown': 'igiene'},
                    {'name': 'Omeopatia',
                     'y': 8,
                     'drilldown': 'omeopatia'}
                ]
            }
        ]
        return series

    @property
    def drilldown(self):
        drilldown = {
            'series': [
                {'id': 'emorroidi',
                 'name': 'Emorroidi',
                 'data': [
                     ['brand1', 7],
                     ['brand2', 3],
                     ['brand3', 5]
                 ]},
                {'id': 'igiene',
                 'name': 'Igiene e Bellezza',
                 'data': [
                     ['brand1', 3],
                     ['brand2', 1],
                     ['brand3', 4],
                     ['brand4', 5]
                 ]},
                {'id': 'omeopatia',
                 'name': 'Omeopatia',
                 'data': [
                     ['brand1', 3],
                     ['brand2', 1],
                     ['brand3', 4],
                     ['', 0]
                 ]}
            ]
        }
        return drilldown

       
```


Then you need to map the graph to an url in url.py file:
```
   from graphs.py import BarView
   url(regex='^bar/$', view=BarView.as_view(), name='bar')
```

In the template:
```
   {% load highcharts_tags %}
   <!-- enable highcharts scripts -->
   <!-- highcharts_js (highcharts 3d highstock heatmap) you need to pass 1 or 0 if you want to enable 3d or highstock         etc...-->
   {% highcharts_js 1 0 0 0 %}
   <!-- the graph container -->
   <div id="container" style="height: 400px; min-width: 310px; max-width: 1200px; margin: 0 auto"></div>
   <!-- the javascript call -->
    $(function () 
            $.getJSON("{% url 'bar' %}", function(data) 
                $('#container').highcharts(data);
            });
    });
```
