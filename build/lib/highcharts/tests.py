from django.utils import simplejson as json
from django.test import TestCase
from highcharts.views.bar import HighChartsBarView, HighChartsStackedView
from highcharts.views.bar import HighChartsColumnView
from highcharts.views.line import HighChartsLineView
from highcharts.views.area import HighChartsAreaView
from django.test import RequestFactory


class EmptyChart(HighChartsLineView):
    pass


class BarDataMixin(object):
    title = u'My Mock Title'
    subtitle = u'My subtitle'
    categories = ['Apples', 'Oranges', 'Pears', 'Grapes', 'Bananas']
    y_axis_title = 'Fruit eaten'
    series = [
        {"name": 'Jane', "data": [5, 3, 4, 7, 2]},
        {"name": 'John', "data": [2, 2, 3, 2, 1]},
        {"name": 'Joe', "data": [3, 4, 4, 2, 5]},
    ]


class MockHighChartsBarView(BarDataMixin, HighChartsBarView):
    pass


class MockHighChartsStackedView(BarDataMixin, HighChartsStackedView):
    pass


class MockHighChartsColumnView(BarDataMixin, HighChartsColumnView):
    pass


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


class MockHighChartsAreaView(HighChartsAreaView):
    title = 'US and USSR nuclear stockpiles'
    y_axis_title = 'Nuclear weapon states'
    tooltip_point_format = '{series.name} produced <b>{point.y:,.0f}</b><br/>'\
                           'warheads in {point.x}'
    plot_options = {
        "area": {
            "pointStart": 1940,
            "marker": {
                "enabled": False,
                "symbol": 'circle',
                "radius": 2,
                "states": {
                    "hover": {
                        "enabled": True
                    }
                }
            }
        }
    }
    series = [{
        "name": 'USA',
        "data": [None, None, None, None, None, 6, 11, 32, 110, 235, 369, 640,
                1005, 1436, 2063, 3057, 4618, 6444, 9822, 15468, 20434, 24126,
                27387, 29459, 31056, 31982, 32040, 31233, 29224, 27342, 26662,
                26956, 27912, 28999, 28965, 27826, 25579, 25722, 24826, 24605,
                24304, 23464, 23708, 24099, 24357, 24237, 24401, 24344, 23586,
                22380, 21004, 17287, 14747, 13076, 12555, 12144, 11009, 10950,
                10871, 10824, 10577, 10527, 10475, 10421, 10358, 10295, 10104]
        }, {
        "name": 'USSR/Russia',
        "data": [
            None, None, None, None, None, None, None, None, None, None,
            5, 25, 50, 120, 150, 200, 426, 660, 869, 1060, 1605, 2471, 3322,
            4238, 5221, 6129, 7089, 8339, 9399, 10538, 11643, 13092, 14478,
            15915, 17385, 19055, 21205, 23044, 25393, 27935, 30062, 32049,
            33952, 35804, 37431, 39197, 45000, 43000, 41000, 39000, 37000,
            35000, 33000, 31000, 29000, 27000, 25000, 24000, 23000, 22000,
            21000, 20000, 19000, 18000, 18000, 17000, 16000]
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


class EmptyOptionsTestCase(ResponseTestToolkitSolo):
    klass = EmptyChart

    def test_title(self):
        self.assertEquals(self.data['title'], {'text': None})

    def test_subtitle(self):
        self.assertNotIn('subtitle', self.data)

    def test_chart(self):
        self.assertEquals(self.data['chart'], {})


class CommonTestCase(ResponseTestToolkit):
    "Testing common properties / results"
    classes = (
        MockHighChartsBarView,
        MockHighChartsStackedView,
        MockHighChartsColumnView,
        HighChartsBarView,
        HighChartsLineView,
        MockHighChartsAreaView,
    )

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
            self.assertIn('text', data['title'])

    def test_chart(self):
        "Test chart data"
        for response in self.responses:
            data = json.loads(response.content)
            self.assertIn('chart', data)
            self.assertTrue(isinstance(data['chart'], dict))


class BarChartTest(ResponseTestToolkitSolo):
    klass = MockHighChartsBarView

    def test_title(self):
        "Test title parameter"
        self.assertEquals(self.data['title'], {'text': u'My Mock Title'})

    def test_subtitle(self):
        "Test subtitle"
        self.assertIn('subtitle', self.data)
        subtitle = self.data['subtitle']
        self.assertIn('text', subtitle)
        self.assertEquals(subtitle['text'], 'My subtitle')

    def test_chart_type(self):
        "Test chart type"
        self.assertEquals(self.data['chart'].get('type', None), 'bar')

    def test_x_axis(self):
        "Test X Axis content"
        self.assertIn('xAxis', self.data)
        x_axis = self.data['xAxis']
        self.assertIn('categories', x_axis)
        categories = x_axis['categories']
        self.assertEquals(
            categories,
            ['Apples', 'Oranges', 'Pears', 'Grapes', 'Bananas']
        )

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
        self.assertEquals(len(series), 3)
        first = series[0]
        self.assertEquals(first['name'], 'Jane')
        self.assertEquals(first['data'], [5, 3, 4, 7, 2])
        second = series[1]
        self.assertEquals(second['name'], 'John')
        self.assertEquals(second['data'], [2, 2, 3, 2, 1])
        second = series[2]
        self.assertEquals(second['name'], 'Joe')
        self.assertEquals(second['data'], [3, 4, 4, 2, 5])


class ColumnChartTest(BarChartTest):
    klass = MockHighChartsColumnView

    def test_chart_type(self):
        "Test chart type"
        self.assertEquals(self.data['chart'].get('type', None), 'column')


class StackedChartTest(BarChartTest):
    klass = MockHighChartsStackedView

    def test_chart_type(self):
        self.assertIn('plotOptions', self.data)
        self.assertIn('series', self.data['plotOptions'])
        self.assertIn('stacking', self.data['plotOptions']['series'])
        self.assertEquals(
            self.data['plotOptions']['series']['stacking'],
            'normal'
        )


class LineChartTest(ResponseTestToolkitSolo):
    klass = MockHighChartsLineView

    def test_title(self):
        "Test title parameter"
        self.assertEquals(self.data['title'], {'text': u'My Line title'})

    def test_chart_type(self):
        "Test chart type"
        self.assertEquals(self.data['chart'].get('type', None), None)

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


class AreaChartTest(ResponseTestToolkitSolo):
    klass = MockHighChartsAreaView

    def test_title(self):
        "Test title parameter"
        self.assertEquals(
            self.data['title'],
            {'text': u'US and USSR nuclear stockpiles'})

    def test_chart_type(self):
        "Test chart type"
        self.assertEquals(self.data['chart'].get('type', None), 'area')

    def test_tooltip(self):
        "Test tooltip"
        self.assertEquals(
            self.data['tooltip'].get('pointFormat'),
            '{series.name} produced <b>{point.y:,.0f}</b>'
            '<br/>warheads in {point.x}'
        )

    def test_plot_options(self):
        "plot options is just dict dumping"
        plot_options = self.data['plotOptions']
        self.assertEquals(plot_options, MockHighChartsAreaView.plot_options)
