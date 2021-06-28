
from django.conf.urls import url, include
from django.contrib import admin
from qa.views import question, index, popular


urlpatterns = [
    url(r'^(?P<num>\d+)/$', question),
]


