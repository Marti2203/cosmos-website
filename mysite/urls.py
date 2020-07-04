# -*- coding: utf-8 -*- from __future__ import absolute_import, print_function, unicode_literals
from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls import include, url
# from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve
from django.contrib.auth import views as auth_views
# from django.conf.urls import patterns
from . import views

admin.autodiscover()

urlpatterns = [
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': {'cmspages': CMSSitemap}}),
    url(r'^admin/', admin.site.urls),
    url(r'^\.well-known/', include('letsencrypt.urls')),
    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), {'next_page': '/'}),
    url(r'^door-status/$', views.display_door_status, name='display_door_status'),
    url(r'^door-status/update/$', views.update_door_status, name='update_door_status'),
    url(r'^pi-ip/update/$', views.update_pi_ip, name='update_pi_ip'),
    url(r'^update-profile/$', views.update_profile, name='update_profile'),
    url(r'^create-member/$', views.create_member, name='create_member'),
    url(r'^requests/$', views.list_requests, name='list_requests'),
    url(r'^accept-request/$', views.accept_request, name='accept_request'),
    url(r'^reject-request/$', views.reject_request, name='reject_request'),
    url(r'^password_reset/$', auth_views.PasswordResetView.as_view(), name='password_reset'),
    url(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetView.as_view(), name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    url(r'^association/photos/[0-9]*/$', views.display_album, name='album'),
    url(r'^', include('cms.urls')),

]

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns += [url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, 'show_indexes': True})] +\
                   staticfiles_urlpatterns()
