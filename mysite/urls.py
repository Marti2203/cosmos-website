# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve
from django.contrib.auth import views as auth_views
from django.conf.urls import patterns
from . import views

admin.autodiscover()

urlpatterns = [
    url(r'^sitemap\.xml$', sitemap,
        {'sitemaps': {'cmspages': CMSSitemap}}),
]


urlpatterns = patterns('',
  url(r'^admin/', include(admin.site.urls)),
  url(r'^login/$', auth_views.login, name='login'),
  url(r'^logout/$', auth_views.logout, {'next_page': '/'}),
  url(r'^update-profile/$', views.update_profile, name='update_profile'),
  url(r'^create-member/$', views.create_member, name='create_member'),
  url(r'^', include('cms.urls')),
)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = [
        url(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ] + staticfiles_urlpatterns() + urlpatterns
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
