from braces.views import JSONResponseMixin, AjaxResponseMixin


class HighChartsBasicView(JSONResponseMixin, AjaxResponseMixin):
    title = None
    subtitle = None
    chart_type = None

    def get_data(self):
        data = {}
        data['title'] = self.title or 'No title'
        if self.subtitle:
            data['subtitle'] = {}
            data['subtitle']['text'] = self.subtitle
        data['chart'] = {}
        if self.chart_type:
            data['chart']['type'] = self.chart_type
        return data

    def get(self, request, *args, **kwargs):
        return self.get_ajax(request, *args, **kwargs)

    def get_ajax(self, request, *args, **kwargs):
        return self.render_json_response(self.get_data())
