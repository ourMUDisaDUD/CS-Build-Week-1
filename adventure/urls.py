from django.conf.urls import url
from . import api

urlpatterns = [
    url('init', api.initialize),
    url('move', api.move),
    url('say', api.say),
    url('getrooms', api.get_rooms),
    url('dup', api.duplicates),
]