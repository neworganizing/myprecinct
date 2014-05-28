from django.conf.urls import patterns, include, url, static
from django.conf import settings
from django.contrib import admin

from myprecinct import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myprecinct.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.HomeView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
)