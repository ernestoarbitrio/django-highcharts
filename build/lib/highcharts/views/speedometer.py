from django.views.generic import View
from highcharts.views.common import HighChartsDualAxisView


class HighChartsSpeedometerView(HighChartsDualAxisView, View):
    chart_type = 'gauge'

    _series = []
    _yaxis = []
    _pane = []

    def get_data(self):
        data = super(HighChartsSpeedometerView, self).get_data()
        data['series'] = self.series
        data['yAxis'] = self.yaxis
        data['pane'] = self.pane
        return data

    @property
    def series(self):
        return self._series

    @property
    def yaxis(self):
        return self._yaxis

    @property
    def pane(self):
        return self._pane

    @series.setter
    def series(self, value):
        self._series = value

    @yaxis.setter
    def yaxis(self, value):
        self._yaxis = value

    @pane.setter
    def pane(self, value):
        self._pane = value