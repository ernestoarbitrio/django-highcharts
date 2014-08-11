from django.views.generic import View
from highcharts.views.common import HighChartsDualAxisView


class HighChartsHeatMapView(HighChartsDualAxisView, View):
    chart_type = 'heatmap'
    margin_top = 40
    margin_bottom = 40
    categories = []
    _series = []
    _yaxis = []
    legend = {'align': 'right',
              'layout': 'vertical',
              'margin': 0,
              'verticalAlign': 'top',
              'y': 25,
              'symbolHeight': 320}

    def get_data(self):
        data = super(HighChartsHeatMapView, self).get_data()
        data['series'] = self.series
        data['yAxis'] = self.yaxis
        data['chart']['marginTop'] = self.margin_top
        data['chart']['marginBottom'] = self.margin_bottom
        data['xAxis']['categories'] = self.categories
        data['legend'] = self.legend
        return data

    @property
    def series(self):
        return self._series

    @property
    def yaxis(self):
        return self._yaxis

    @series.setter
    def series(self, value):
        self._series = value

    @yaxis.setter
    def yaxis(self, value):
        self._yaxis = value