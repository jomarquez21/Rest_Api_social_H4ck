from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from views import *

urlpatterns = [
    url(r'^user/$', csrf_exempt(ViewUser.as_view())),
    url(r'^user/(?P<user>[\d]+)/$', csrf_exempt(ViewUser.as_view())),
    url(r'^user/all/$', csrf_exempt(ViewUserAll.as_view())),
]
