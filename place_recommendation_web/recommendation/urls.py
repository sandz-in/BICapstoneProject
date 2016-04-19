from recommendation.views import home_view

__author__ = 'sandz'
from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^$', home_view, name='home'),
                       )
