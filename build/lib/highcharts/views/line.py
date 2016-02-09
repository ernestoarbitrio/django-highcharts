from django.views.generic import View
from highcharts.views.common import HighChartsDualAxisView


class HighChartsLineView(HighChartsDualAxisView, View):
    categories = []
    _series = []

    def get_data(self):
        data = super(HighChartsLineView, self).get_data()
        data['xAxis']['categories'] = self.categories
        data['series'] = self.series
        return data

    @property
    def series(self):
        return self._series

    @series.setter
    def series(self, value):
        self._series = value