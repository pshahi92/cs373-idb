from django.conf.urls import patterns, include, url
from django.conf import settings
from wc_app import views

from django.contrib import admin
from wc_app.api import *
from wc_app.views import handler404

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'world_cup.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #Home and admin
    url(r'^$', views.home, name='home'),
    url(r'^admin/', include(admin.site.urls)),

    #Dynamic data
    #this is the parent countries url
    url(r'^countries/$', views.countries, name='countries'),
    #this one is a for a specfic country
    url(r'^countries/(?P<c_name>\w+)/$', views.country, name='country'), 
    
    #this is the parent players url
    url(r'^players/$', views.players, name='players'),
    #this one is a for a specfic player
    url(r'^players/(?P<p_name>[\w]+)/$', views.player, name='player'),
    
    #this is the parent matches url
    url(r'^matches/$', views.matches, name='matches'),
    #this one is a for a specfic match
    url(r'^matches/(\d+)/$', views.match, name='match'),
    
    url(r'^aboutus/$', views.aboutus, name='aboutus'),


    #RESTful API
    url(r'^api/', include(CountryResource().urls)),
    url(r'^api/', include(PlayerResource().urls)),
    url(r'^api/', include(MatchResource().urls)),

    #Error 404
    url(r'./$', views.handler404, name='handler404')
    
    #For testing stuff
    #url(r'^test/$', views.test, name='test'),
)