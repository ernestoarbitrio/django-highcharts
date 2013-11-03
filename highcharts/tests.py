from django.utils import simplejson as json
from django.test import TestCase
from highcharts.views.bar import HighChartsBarView
from django.test import RequestFactory


class MockHighChartsBarView(HighChartsBarView):
    title = u'My Mock Title'
    categories = ['Apples', 'Bananas', 'Oranges']
    y_axis_title = 'Fruit eaten'
    series = [
        {"name": 'Jane', "data": [1, 0, 4]},
        {"name": 'John', "data": [5, 7, 3]}
    ]


class ResponseTestToolkit(TestCase):
    "Generic toolkit for tests. Uses multiple classes as a class property."
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
    "Generic toolkit for tests. Uses one `klass` class property"

    @property
    def response(self):
        return self.get_view(self.klass)(self.request)

    @property
    def data(self):
        return json.loads(self.response.content)


class CommonTestCase(ResponseTestToolkit):
    "Testing common properties / results"
    classes = (MockHighChartsBarView, HighChartsBarView,)

    def test_status_code(self):
        "Test view status code"
        for response in self.responses:
            self.assertEquals(response.status_code, 200)
            self.assertTrue(response.content)

    def test_json(self):
        "Test the JSON response"
        for response in self.responses:
            headers = response.serialize_headers()
            self.assertIn('application/json', headers)

    def test_title(self):
        "Test the title content"
        for response in self.responses:
            data = json.loads(response.content)
            self.assertIn('title', data)


class BarChartTest(ResponseTestToolkitSolo):
    klass = MockHighChartsBarView

    def test_title(self):
        "Test title parameter"
        self.assertEquals(self.data['title'], u'My Mock Title')

    def test_x_axis(self):
        "Test X Axis content"
        self.assertIn('xAxis', self.data)
        x_axis = self.data['xAxis']
        self.assertIn('categories', x_axis)
        categories = x_axis['categories']
        self.assertEquals(categories, ['Apples', 'Bananas', 'Oranges'])

    def test_y_axis(self):
        "Test Y Axis content"
        self.assertIn('yAxis', self.data)
        y_axis = self.data['yAxis']
        self.assertEquals(y_axis, {"title": {"text": 'Fruit eaten'}})

    def test_series(self):
        "Test data from series"
        self.assertIn('series', self.data)
        series = self.data['series']
        self.assertTrue(isinstance(series, (list, tuple, set)))
        self.assertEquals(len(series), 2)
        first = series[0]
        self.assertEquals(first['name'], 'Jane')
        self.assertEquals(first['data'], [1, 0, 4])
        second = series[1]
        self.assertEquals(second['name'], 'John')
        self.assertEquals(second['data'], [5, 7, 3])
