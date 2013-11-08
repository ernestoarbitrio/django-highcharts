from django.views.generic import View
from highcharts.views.common import HighChartsDualAxisView


class HighChartsLineView(HighChartsDualAxisView, View):
    categories = []

    def get_data(self):
        data = super(HighChartsLineView, self).get_data()
        data['xAxis']['categories'] = self.categories
        data['yAxis'] = self.y_axis
        data['yAxis']['title'] = {"text": self.y_axis_title}
        data['series'] = self.series
        return data

    @property
    def series(self):
        return []
