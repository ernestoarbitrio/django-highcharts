from braces.views import JSONResponseMixin, AjaxResponseMixin


class HighChartsBasicView(JSONResponseMixin, AjaxResponseMixin):
    title = None
    title_style = None
    subtitle = None
    chart_type = None
    tooltip = None
    tooltip_point_format = None
    plot_options = {}
    chart = {}
    legend = True
    credits = {
            'enabled': False
        }
    coloraxis = {}
    exporting = {
        'sourceWidth': 1600,
        'sourceHeight': 900,
        'chartOptions': {
            'subtitle': None
        }
    }

    def get_data(self):
        data = dict()
        # Title of the graph

        data['title'] = {}
        data['title']['text'] = self.title or None
        data['title']['style'] = self.title_style or {}
        data['colorAxis'] = self.coloraxis
        data['exporting'] = self.exporting
        data['credits'] = self.credits
        # Subtitle option
        if self.subtitle:
            data['subtitle'] = {}
            data['subtitle']['text'] = self.subtitle

        # Chart type option
        # Chart object to define options such as zoomType
        data['chart'] = self.chart
        if self.chart_type:
            data['chart']['type'] = self.chart_type

        # tooltip
        if self.tooltip or self.tooltip_point_format:
            if not self.tooltip:
                self.tooltip = {}
            data['tooltip'] = self.tooltip
            if self.tooltip_point_format:
                data['tooltip']['pointFormat'] = self.tooltip_point_format

        # plotOptions is just dict dumping
        if self.plot_options:
            data['plotOptions'] = self.plot_options

        data['legend'] = self.legend

        return data

    def get(self, request, *args, **kwargs):
        return self.get_ajax(request, *args, **kwargs)

    def get_ajax(self, request, *args, **kwargs):
        return self.render_json_response(self.get_data())


class HighChartsDualAxisView(HighChartsBasicView):
    y_axis = {}
    y_axis_title = None

    def get_data(self):
        data = super(HighChartsDualAxisView, self).get_data()
        data['xAxis'] = {}
        data['yAxis'] = self.y_axis
        #data['yAxis']['title'] = {"text": str(self.y_axis_title)}
        return data
