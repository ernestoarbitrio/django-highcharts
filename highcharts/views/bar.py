from highcharts.views import HighChartsBasicView
from django.views.generic import View


class HighChartsBarView(HighChartsBasicView, View):
    x_axis = {'categories': []}
    y_axis = {}

    def get_data(self):
        data = super(HighChartsBarView, self).get_data()
        data['xAxis'] = self.x_axis
        data['yAxis'] = self.y_axis
        data['series'] = self.series
        return data

    @property
    def series(self):
        return []
