from highcharts.views import HighChartsBasicView
from django.views.generic import View


class HighChartsBarView(HighChartsBasicView, View):
    x_axis = {'categories': []}

    def get_data(self):
        data = super(HighChartsBarView, self).get_data()
        data['xAxis'] = self.x_axis
        return data
