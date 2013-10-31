from highcharts.views import HighChartsBasicView
from django.views.generic import View


class HighChartsBarView(HighChartsBasicView, View):
    chart = {"type": 'bar'}
    categories = []
    y_axis = {}

    def get_data(self):
        data = super(HighChartsBarView, self).get_data()
        data['chart'] = self.chart
        data['xAxis'] = {}
        data['xAxis']['categories'] = self.categories
        data['yAxis'] = self.y_axis
        data['series'] = self.series
        return data

    @property
    def series(self):
        return []
