from django.utils import simplejson as json
from django.test import TestCase
from highcharts.views.bar import HighChartsBarView
from highcharts.views.line import HighChartsLineView
from django.test import RequestFactory


class MockHighChartsBarView(HighChartsBarView):
    title = u'My Mock Title'
    categories = ['Apples', 'Bananas', 'Oranges']
    y_axis_title = 'Fruit eaten'
    series = [
        {"name": 'Jane', "data": [1, 0, 4]},
        {"name": 'John', "data": [5, 7, 3]}
    ]


class MockHighChartsLineView(HighChartsLineView):
    title = u"My Line title"
    categories = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                  'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    @property
    def series(self):
        return [{
            "name": 'Tokyo',
            "data": [7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2,
                     26.5, 23.3, 18.3, 13.9, 9.6]
        }, {
            "name": 'New York',
            "data": [-0.2, 0.8, 5.7, 11.3, 17.0, 22.0, 24.8, 24.1, 20.1, 14.1,
                     8.6, 2.5]
        }, {
            "name": 'Berlin',
            "data": [-0.9, 0.6, 3.5, 8.4, 13.5, 17.0, 18.6, 17.9, 14.3, 9.0,
                     3.9, 1.0]
        }, {
            "name": 'London',
            "data": [3.9, 4.2, 5.7, 8.5, 11.9, 15.2, 17.0, 16.6, 14.2, 10.3,
                     6.6, 4.8]
        }]


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
    classes = (MockHighChartsBarView, HighChartsBarView, HighChartsLineView)

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


class LineChartTest(ResponseTestToolkitSolo):
    klass = MockHighChartsLineView

    def test_title(self):
        "Test title parameter"
        self.assertEquals(self.data['title'], u'My Line title')

    def test_x_axis(self):
        "Test X Axis content"
        self.assertIn('xAxis', self.data)
        x_axis = self.data['xAxis']
        self.assertIn('categories', x_axis)
        categories = x_axis['categories']
        self.assertEquals(
            categories,
            ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep',
             'Oct', 'Nov', 'Dec'])

    def test_series(self):
        "Test data from series"
        self.assertIn('series', self.data)
        series = self.data['series']
        self.assertTrue(isinstance(series, (list, tuple, set)))
        self.assertEquals(len(series), 4)
        first = series[0]
        self.assertEquals(first['name'], 'Tokyo')
        self.assertEquals(
            first['data'],
            [7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9,
             9.6])
        second = series[1]
        self.assertEquals(second['name'], 'New York')
        self.assertEquals(
            second["data"],
            [-0.2, 0.8, 5.7, 11.3, 17.0, 22.0, 24.8, 24.1, 20.1, 14.1, 8.6,
             2.5])
        third = series[2]
        self.assertEquals(third['name'], "Berlin")
        self.assertEquals(
            third["data"],
            [-0.9, 0.6, 3.5, 8.4, 13.5, 17.0, 18.6, 17.9, 14.3, 9.0, 3.9, 1.0])
        fourth = series[3]
        self.assertEquals(fourth["name"], 'London')
        self.assertEquals(
            fourth["data"],
            [3.9, 4.2, 5.7, 8.5, 11.9, 15.2, 17.0, 16.6, 14.2, 10.3, 6.6, 4.8])
