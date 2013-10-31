from django.utils import simplejson as json
from django.test import TestCase
from highcharts.views.bar import HighChartsBarView
from django.test import RequestFactory


class MockHighChartsBarView(HighChartsBarView):
    title = u'My Mock Title'
    x_axis = {"categories": ['Apples', 'Bananas', 'Oranges']}
    y_axis = {"title": {"text": 'Fruit eaten'}}
    series = [
        {"name": 'Jane', "data": [1, 0, 4]},
        {"name": 'John', "data": [5, 7, 3]}
    ]


class ResponseTestToolkit(TestCase):

    @property
    def request(self):
        request_factory = RequestFactory()
        return request_factory.get('/bar')

    def get_view(self, klass):
        return klass.as_view()

    @property
    def responses(self):
        for klass in self.classes:
            yield self.get_view(klass)(self.request)


class ResponseTestToolkitSolo(ResponseTestToolkit):

    @property
    def response(self):
        return self.get_view(self.klass)(self.request)

    @property
    def data(self):
        return json.loads(self.response.content)


class BasicTests(ResponseTestToolkit):

    classes = (MockHighChartsBarView, HighChartsBarView,)

    def test_status_code(self):
        for response in self.responses:
            self.assertEquals(response.status_code, 200)
            self.assertTrue(response.content)

    def test_title(self):
        for response in self.responses:
            data = json.loads(response.content)
            self.assertIn('title', data)


class BarChartTest(ResponseTestToolkitSolo):
    klass = MockHighChartsBarView

    def test_title(self):
        self.assertEquals(self.data['title'], u'My Mock Title')

    def test_x_axis(self):
        self.assertIn('xAxis', self.data)
        x_axis = self.data['xAxis']
        self.assertIn('categories', x_axis)
        categories = x_axis['categories']
        self.assertEquals(categories, ['Apples', 'Bananas', 'Oranges'])

    def test_y_axis(self):
        self.assertIn('yAxis', self.data)
        y_axis = self.data['yAxis']
        self.assertEquals(y_axis, {"title": {"text": 'Fruit eaten'}})

    def test_series(self):
        # series = [
        #     {"name": 'Jane', "data": [1, 0, 4]},
        #     {"name": 'John', "data": [5, 7, 3]}
        # ]
        self.assertIn('series', self.data)
        series = self.data['series']
        self.assertTrue(isinstance(series, (list, tuple, set)))
        self.assertEquals(len(series), 2)
