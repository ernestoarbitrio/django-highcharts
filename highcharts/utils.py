from django.conf import settings


def get_static_url(subfix='highcharts'):
    static_url = getattr(settings, 'STATIC_URL', None)
    if static_url:
        return static_url
    else:  # To old django versions
        return '%s%s/' % (getattr(settings, 'MEDIA_URL', None), subfix)
