from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
   # Uncomment the admin/doc line below to enable admin documentation:
   url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

   # Uncomment the next line to enable the admin:
   url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('apps.devproc.views.requirement',
   url(r'^requirements/$', 'view_all_reqmts'),
   url(r'^requirements/add/$', 'create_reqmt'),
   url(r'^requirements/(?P<reqmt_id>\d+)/$', 'view_reqmt'),
   url(r'^requirements/(?P<reqmt_id>\d+)/edit/$', 'edit_reqmt'),
)

urlpatterns += patterns('apps.devproc.views.attribute',
   url(r'^attributes/$', 'view_all_attributes'),
   url(r'^attributes/add/$', 'create_attribute'),
   url(r'^attributes/(?P<attribute_id>\d+)/$', 'view_attribute'),
   url(r'^attributes/(?P<attribute_id>\d+)/edit/$', 'edit_attribute'),
)

urlpatterns += patterns('apps.devproc.views.betatest',
   url(r'^betatests/$', 'view_all_betatests'),
   url(r'^betatests/add/$', 'create_betatest'),
   url(r'^betatests/(?P<betatest_id>\d+)/$', 'view_betatest'),
   url(r'^betatests/(?P<betatest_id>\d+)/edit/$', 'edit_betatest'),
)

urlpatterns += patterns('apps.devproc.views.bug',
   url(r'^bugs/$', 'view_all_bugs'),
   url(r'^bugs/add/$', 'create_bug'),
   url(r'^bugs/(?P<bug_id>\d+)/$', 'view_bug'),
   url(r'^bugs/(?P<bug_id>\d+)/edit/$', 'edit_bug'),
)

urlpatterns += patterns('apps.devproc.views.component',
   url(r'^components/$', 'view_all_component'),
   url(r'^components/add/$', 'create_component'),
   url(r'^components/(?P<component_id>\d+)/$', 'view_component'),
   url(r'^components/(?P<component_id>\d+)/edit/$', 'edit_component'),
)








