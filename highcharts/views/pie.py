from django.views.generic import View
from highcharts.views.common import HighChartsBasicView


class HighChartsPieView(HighChartsBasicView, View):
    chart_type = 'pie'

    def get_data(self):
        data = super(HighChartsPieView, self).get_data()
        data['series'] = self.series
        data['drilldown'] = self.drilldown
        return data

    @property
    def series(self):
        return []

    @property
    def drilldown(self):
        return []