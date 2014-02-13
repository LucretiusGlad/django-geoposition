from django.conf import settings
from appconf import AppConf


class GeopositionConf(AppConf):
    MAP_WIDGET_HEIGHT = 480
    JS_SCROLLWHEEL = True
    JS_DEFAULT_LATITUDE = 0
    JS_DEFAULT_LONGITUDE = 0
    JS_DEFAULT_ZOOM = 15
    

    class Meta:
        prefix = 'geoposition'