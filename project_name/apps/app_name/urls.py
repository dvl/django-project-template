# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from .views import ModelNameListView, ModelNameDetailView, ModelNameCreateView,\
    ModelNameDeleteView, ModelNameUpdateView

urlpatterns = patterns(
    '',

    url(r'^list/$', ModelNameListView.as_view(), name='list'),
    url(r'^detail/(?P<pk>.*)/$', ModelNameDetailView.as_view(), name='detail'),
    url(r'^create/$', ModelNameCreateView.as_view(), name='create'),
    url(r'^update/(?P<pk>.*)/$', ModelNameUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>.*)/$', ModelNameDeleteView.as_view(), name='delete'),
)
