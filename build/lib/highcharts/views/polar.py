from django.views.generic import View
from highcharts.views.common import HighChartsDualAxisView


class HighChartsPolarView(HighChartsDualAxisView, View):
    chart_type = 'line'
    polar = True
    pane_size = '80%'
    categories = []
    _series = []
    _yaxis = []
    legend = {
        'align': 'right',
        'verticalAlign': 'top',
        'y': 70,
        'layout': 'vertical'
    }
    tickmarkPlacement = 'on'
    lineWidth = 0

    def get_data(self):
        data = super(HighChartsPolarView, self).get_data()
        data['series'] = self.series
        data['yAxis'] = self.yaxis
        data['chart']['polar'] = self.polar
        data['pane'] = self.pane_size
        data['xAxis']['categories'] = self.categories
        data['xAxis']['tickmarkPlacement'] = self.tickmarkPlacement
        data['xAxis']['lineWidth'] = self.lineWidth
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