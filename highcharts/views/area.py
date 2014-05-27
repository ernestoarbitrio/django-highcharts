from django.views.generic import View
from highcharts.views.common import HighChartsDualAxisView


class HighChartsAreaView(HighChartsDualAxisView, View):
    chart_type = 'area'
    _series = []

    def get_data(self):
        data = super(HighChartsAreaView, self).get_data()
        data['series'] = self.series
        return data

    @property
    def series(self):
        return self._series

    @series.setter
    def series(self, value):
        self._series = value
