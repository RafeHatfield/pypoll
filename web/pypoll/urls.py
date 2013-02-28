from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

# urlpatterns = patterns('',
#     url(r'^polls/$', 'polls.views.index'),
#     url(r'^polls/(?P<poll_id>\d+)/$', 'polls.views.detail'),
#     url(r'^polls/(?P<poll_id>\d+)/results/$', 'polls.views.results'),
#     url(r'^polls/(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
#     url(r'^admin/', include(admin.site.urls)),
# )

# urlpatterns = patterns('polls.views',
#     url(r'^polls/$', 'index'),
#     url(r'^polls/(?P<poll_id>\d+)/$', 'detail'),
#     url(r'^polls/(?P<poll_id>\d+)/results/$', 'results'),
#     url(r'^polls/(?P<poll_id>\d+)/vote/$', 'vote'),
# )

# urlpatterns += patterns('',
#   url(r'^admin/', include(admin.site.urls))
# )

urlpatterns = patterns('',
  url(r'^polls/', include('polls.urls')),
  url(r'^admin/', include(admin.site.urls))
)

