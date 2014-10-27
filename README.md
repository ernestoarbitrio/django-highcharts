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



