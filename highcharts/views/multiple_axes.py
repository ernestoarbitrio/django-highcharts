from django.views.generic import View
from highcharts.views.common import HighChartsDualAxisView


class HighChartsMultiAxesView(HighChartsDualAxisView, View):

    chart_type = ''
    categories = []
    xlabels = {'rotation': -45}
    plotlines = None
    _series = []
    _yaxis = []
    def get_data(self):
        data = super(HighChartsMultiAxesView, self).get_data()
        data['xAxis']['categories'] = self.categories
        data['xAxis']['labels'] = self.xlabels
        data['xAxis']['plotLines'] = self.plotlines
        data['series'] = self.series
        data['yAxis'] = self.yaxis
        return data

    @property
    def series(self):
        return self._series

    @property
    def yaxis(self):
        return self._yaxis

    @series.setter
    def series(self, value):
        self._series = value

    @yaxis.setter
    def yaxis(self, value):
        self._yaxis = value


class HighChartsStockView(HighChartsDualAxisView, View):

    chart_type = ''
    categories = []
    plotlines = None
    _series = []
    _yaxis = []
    _xaxis = []
    def get_data(self):
        data = super(HighChartsStockView, self).get_data()
        data['series'] = self.series
        data['yAxis'] = self.yaxis
        data['xAxis'] = {}
        print data['xAxis']
        print 'cass'
        return data

    @property
    def series(self):
        return self._series

    @property
    def yaxis(self):
        return self._yaxis

    @series.setter
    def series(self, value):
        self._series = value

    @yaxis.setter
    def yaxis(self, value):
        self._yaxis = value

    @property
    def xaxis(self):
        return self._xaxis

    @yaxis.setter
    def xaxis(self, value):
        self._xaxis = value


class HighChartsStackedView(HighChartsMultiAxesView):

    @property
    def plot_options(self):
        plot_options = super(HighChartsMultiAxesView, self).plot_options
        if plot_options is None:
            plot_options = {}
        if 'series' not in plot_options:
            plot_options['series'] = {}
        plot_options['series']['stacking'] = 'normal'
        return plot_options


class HighChartsColumnView(HighChartsMultiAxesView):
    chart_type = 'column'