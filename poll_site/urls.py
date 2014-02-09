from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^polls/$', 'poll.views.index', name='home'),
    url(r'^polls/(?P<poll_id>\d+)/$', 'poll.views.detail', name='detail'),
    #url(r'^(?P<pk>\d+)/results/$', 'poll.views.results, name='results'),
    #url(r'^(?P<poll_id>\d+)/vote/$', 'poll.views.vote, name='vote'),
    url(r'^contact/thankyou/', 'poll.views.thankyou', name='thankyou'),
    url(r'^contact/', 'poll.views.contact', name='contact'),
    # url(r'^poll_site/', include('poll_site.foo.urls')),

    url(r'^wikicamp/(?P<page_name>\w+)/$', 'appwiki.views.view_page'),
    url(r'^wikicamp/(?P<page_name>\w+)/edit/$', 'appwiki.views.edit_page'),
    url(r'^wikicamp/(?P<page_name>\w+)/save/$', 'appwiki.views.save_page'),
    url(r'^wikicamp/(?P<page_name>\w+)/search/$', 'appwiki.views.search_page'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
