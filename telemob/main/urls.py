# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('main',

	url(r'^$', 'views.index', name='index'),
	url(r'^politicos/(?P<campaign_id>\d+)/$', 'views.politician_list', name='state_list'),
	url(r'^politicos/(?P<campaign_id>\d+)/(?P<uf>\w+)/$', 'views.politician_list', name='politician_list'),
	url(r'^relatorio/(?P<campaign_id>\d+)/(?P<politician_id>\d+)/$', 'views.report_contact', name='report_contact'),

)
