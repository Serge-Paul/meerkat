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

urlpatterns += patterns('apps.public.views.auth',
#  url(r'^accounts/signup/$', 'account_signup'),
  url(r'^accounts/login/$', 'process_login'),
  url(r'^accounts/logout/$', 'process_logout'),
)


urlpatterns += patterns('apps.devproc.views.feedback',
   url(r'^feedback/$', 'view_all_feedback'),
   url(r'^feedback/add/(?P<feature_id>\d+)/$', 'create_feedback'),
   url(r'^feedback/(?P<betatest_id>\d+)/(?P<customer_id>\d+)/$', 'view_feedback'),
   url(r'^feedback/(?P<feedback_id>\d+)/edit/$', 'edit_feedback'),
   url(r'^feedback/(?P<feedback_id>\d+)/delete/$', 'delete_feedback'),
)


urlpatterns += patterns('apps.devproc.views.requirement',
   url(r'^requirements/$', 'view_all_reqmts'),
   url(r'^requirements/add/$', 'create_reqmt'),
   url(r'^requirements/(?P<reqmt_id>\d+)/$', 'view_reqmt'),
   url(r'^requirements/(?P<reqmt_id>\d+)/edit/$', 'edit_reqmt'),
   url(r'^requirements/(?P<reqmt_id>\d+)/delete/$', 'delete_reqmt'),
)


urlpatterns += patterns('apps.devproc.views.attribute',
   url(r'^attributes/(?P<component_id>\d+)/$', 'view_all_attributes'),
   url(r'^attributes/add/(?P<component_id>\d+)/$', 'create_attribute'),
   url(r'^attributes/(?P<component_id>\d+)/(?P<attribute_id>\d+)/$', 'view_attribute'),
   url(r'^attributes/(?P<attribute_id>\d+)/edit/$', 'edit_attribute'),
   url(r'^attributes/(?P<attribute_id>\d+)/delete/$', 'delete_attribute'),
)


urlpatterns += patterns('apps.devproc.views.betatest',
   url(r'^betatests/$', 'view_all_betatests'),
   url(r'^betatests/add/$', 'create_betatest'),
   url(r'^betatests/(?P<betatest_id>\d+)/$', 'view_betatest'),
   url(r'^betatests/(?P<betatest_id>\d+)/edit/$', 'edit_betatest'),
   url(r'^betatests/(?P<betatest_id>\d+)/delete/$', 'delete_betatest'),
)


urlpatterns += patterns('apps.devproc.views.bug',
   url(r'^bugs/$', 'view_all_bugs'),
   url(r'^bugs/add/test/(?P<test_id>\d+)/$', 'create_bug', {'type': 'test'}),
   url(r'^bugs/add/betatest/(?P<test_id>\d+)/$', 'create_bug', {'type': 'betatest'}),
   url(r'^bugs/(?P<bug_id>\d+)/$', 'view_bug'),
   url(r'^bugs/(?P<bug_id>\d+)/edit/$', 'edit_bug'),
   url(r'^bugs/(?P<bug_id>\d+)/delete/$', 'delete_bug'),
)

urlpatterns += patterns('apps.devproc.views.component',
   url(r'^components/$', 'view_all_components'),
   url(r'^components/add/$', 'create_component'),
   url(r'^components/(?P<component_id>\d+)/$', 'view_component'),
   url(r'^components/(?P<component_id>\d+)/edit/$', 'edit_component'),
   url(r'^components/(?P<component_id>\d+)/delete/$', 'delete_component'),
)

urlpatterns += patterns('apps.devproc.views.customer',
   url(r'^customers/$', 'view_all_customers'),
   url(r'^customers/add/$', 'create_customer'),
   url(r'^customers/(?P<customer_id>\d+)/$', 'view_customer'),
   url(r'^customers/(?P<customer_id>\d+)/edit/$', 'edit_customer'),
   url(r'^customers/(?P<customer_id>\d+)/delete/$', 'delete_customer'),
)

urlpatterns += patterns('apps.devproc.views.feature',
   url(r'^features/$', 'view_all_features'),
   url(r'^features/add/$', 'create_feature'),
   url(r'^features/(?P<feature_id>\d+)/$', 'view_feature'),
   url(r'^features/(?P<feature_id>\d+)/edit/$', 'edit_feature'),
   url(r'^features/(?P<feature_id>\d+)/delete/$', 'delete_feature'),
)

urlpatterns += patterns('apps.devproc.views.member',
   url(r'^members/team/(?P<team_id>\d+)/$', 'view_all_members'),
   url(r'^members/(?P<team_id>\d+)/add/$', 'create_member'),
   url(r'^members/(?P<member_id>\d+)/$', 'view_member'),
   url(r'^members/(?P<member_id>\d+)/edit/$', 'edit_member'),
   url(r'^members/(?P<member_id>\d+)/delete/$', 'delete_member'),
)

urlpatterns += patterns('apps.devproc.views.milestone',
   url(r'^milestones/$', 'view_all_milestones'),
   url(r'^milestones/add/$', 'create_milestone'),
   url(r'^milestones/(?P<milestone_id>\d+)/$', 'view_milestone'),
   url(r'^milestones/(?P<milestone_id>\d+)/edit/$', 'edit_milestone'),
   url(r'^milestones/(?P<milestone_id>\d+)/delete/$', 'delete_milestone'),
)

urlpatterns += patterns('apps.devproc.views.release',
   url(r'^releases/$', 'view_all_releases'),
   url(r'^releases/add/$', 'create_release'),
   url(r'^releases/(?P<release_id>\d+)/$', 'view_release'),
   url(r'^releases/(?P<release_id>\d+)/edit/$', 'edit_release'),
   url(r'^releases/(?P<release_id>\d+)/delete/$', 'delete_release'),
)


urlpatterns += patterns('apps.devproc.views.risk',
   url(r'^risks/$', 'view_all_risks'),
   url(r'^risks/add/feature/(?P<obj_id>\d+)/$', 'create_risk', {'type': 'feature'}),
   url(r'^risks/add/component/(?P<obj_id>\d+)/$', 'create_risk', {'type': 'component'}),
   url(r'^risks/add/bug/(?P<obj_id>\d+)/$', 'create_risk', {'type': 'bug'}),
   url(r'^risks/(?P<risk_id>\d+)/$', 'view_risk'),
   url(r'^risks/(?P<risk_id>\d+)/edit/$', 'edit_risk'),
   url(r'^risks/(?P<risk_id>\d+)/delete/$', 'delete_risk'),
)


urlpatterns += patterns('apps.devproc.views.roadmap',
   url(r'^roadmap/$', 'view_roadmap')
)

urlpatterns += patterns('apps.devproc.views.team',
   url(r'^teams/$', 'view_all_teams'),
   url(r'^teams/add/$', 'create_team'),
   url(r'^teams/(?P<team_id>\d+)/$', 'view_team'),
   url(r'^teams/(?P<team_id>\d+)/edit/$', 'edit_team'),
   url(r'^teams/(?P<team_id>\d+)/delete/$', 'delete_team'),
)

urlpatterns += patterns('apps.devproc.views.test',
   url(r'^tests/$', 'view_all_tests'),
   url(r'^tests/add/$', 'create_test'),
   url(r'^tests/(?P<test_id>\d+)/$', 'view_test'),
   url(r'^tests/(?P<test_id>\d+)/edit/$', 'edit_test'),
   url(r'^tests/(?P<test_id>\d+)/delete/$', 'delete_test'),
)


urlpatterns += patterns('apps.devproc.views.usecase',
   url(r'^usecases/$', 'view_all_usecases'),
   url(r'^usecases/add/$', 'create_usecase'),
   url(r'^usecases/(?P<usecase_id>\d+)/$', 'view_usecase'),
   url(r'^usecases/(?P<usecase_id>\d+)/edit/$', 'edit_usecase'),
   url(r'^usecases/(?P<usecase_id>\d+)/delete/$', 'delete_usecase'),
)








































