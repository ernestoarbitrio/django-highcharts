from django.views.generic import View
from highcharts.views.common import HighChartsBasicView


class HighChartsPieView(HighChartsBasicView, View):
    chart_type = 'pie'
    options3d = ''
    _series = []
    _drilldown = []

    def get_data(self):
        data = super(HighChartsPieView, self).get_data()
        data['series'] = self.series
        data['drilldown'] = self.drilldown
        data['chart']['options3d'] = self.options3d
        return data

    @property
    def series(self):
        return self._series

    @property
    def drilldown(self):
        return self._drilldown

    @series.setter
    def series(self, value):
        self._series = value

    @drilldown.setter
    def drilldown(self, value):
        self._drilldown = value