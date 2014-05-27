from django.views.generic import View
from highcharts.views.common import HighChartsDualAxisView


class HighChartsBarView(HighChartsDualAxisView, View):
    chart_type = 'bar'
    categories = []
    _series = []

    def get_data(self):
        data = super(HighChartsBarView, self).get_data()
        data['xAxis']['categories'] = self.categories
        data['series'] = self.series
        return data

    @property
    def series(self):
        return self._series

    @series.setter
    def series(self, value):
        self._series = value


class HighChartsStackedView(HighChartsBarView):

    @property
    def plot_options(self):
        plot_options = super(HighChartsBarView, self).plot_options
        if plot_options is None:
            plot_options = {}
        if 'series' not in plot_options:
            plot_options['series'] = {}
        plot_options['series']['stacking'] = 'normal'
        return plot_options


class HighChartsColumnView(HighChartsBarView):
    chart_type = 'column'
