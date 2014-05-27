from django.views.generic import View
from highcharts.views.common import HighChartsDualAxisView


class HighChartsSpeedometerView(HighChartsDualAxisView, View):
    chart_type = 'gauge'

    def get_data(self):
        data = super(HighChartsSpeedometerView, self).get_data()
        data['series'] = self.series
        data['yAxis'] = self.yaxis
        data['pane'] = self.pane
        return data

    @property
    def series(self):
        return []

    @property
    def yaxis(self):
        return []

    @property
    def pane(self):
        return []