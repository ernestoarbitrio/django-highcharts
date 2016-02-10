__author__ = 'ernesto.arbitrio@gmail.com'

from django.template import Library
from ..utils import get_static_url

register = Library()


def highcharts_js(context,
                  activate_highcharts=True,
                  enable_highstock=False,
                  enable_3d=False,
                  enable_heatmap=False):
    return {
        'STATIC_URL': get_static_url(),
        'activate_highcharts': activate_highcharts,
        'enable_highstock': enable_highstock,
        'enable_3d': enable_3d,
        'enable_heatmap': enable_heatmap
    }


def set_highcharts_theme(context, theme_name=None):
    return {
        'STATIC_URL': get_static_url(),
        'theme_name': '{}{}'.format(theme_name, '.js')
    }
register.inclusion_tag("highcharts/highcharts_js.html", takes_context=True)(highcharts_js)
register.inclusion_tag("highcharts/highcharts_theme.html", takes_context=True)(set_highcharts_theme)
