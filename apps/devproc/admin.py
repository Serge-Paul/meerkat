from meerkat.apps.devproc.models import *
from django.contrib import admin

class RequirementAdmin(admin.ModelAdmin):
  list_display = ('id','title', 'priority', 'approval_status')
  search_fields = ['id', 'title','description', 'category']
admin.site.register(Requirement, RequirementAdmin)

class CategoryAdmin(admin.ModelAdmin):
  list_display = ('category', 'id')
  search_fields = ['id', 'category']
admin.site.register(Category, CategoryAdmin)

class UseCaseAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'description', 'target_market', 'target_user')
  search_fields = ['id', 'title', 'description','category','target_market', 'target_user']
admin.site.register(UseCase, UseCaseAdmin)

class AttributeAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'description')
  search_fields = ['id', 'title', 'description']
admin.site.register(Attribute, AttributeAdmin)

class ComponentAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'description', 'approval_status')
  search_fields = ['id', 'title', 'description', 'category', 'approval_status']
admin.site.register(Component, ComponentAdmin)

class FeatureAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'description', 'approval_status')
  search_fields = ['id', 'title', 'description', 'category', 'approval_status']
admin.site.register(Feature, FeatureAdmin)

class TestAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'description', 'status')
  search_fields = ['id', 'title', 'description', 'category', 'status']
admin.site.register(Test, TestAdmin)

class BugAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'description', 'status', 'severity')
  search_fields = ['id', 'title', 'description', 'status', 'severity']
admin.site.register(Bug, BugAdmin)

class BetaTestAdmin(admin.ModelAdmin):
  list_display = ('id', 'feedback')
  search_fields = ['id', 'customer', 'feedback', 'features']
admin.site.register(BetaTest, BetaTestAdmin)

class CustomerAdmin(admin.ModelAdmin):
  list_display = ('id', 'first_name', 'last_name', 'organization')
  search_fields = ['id', 'first_name', 'last_name', 'organization']
admin.site.register(Customer, CustomerAdmin)

class ReleaseAdmin(admin.ModelAdmin):
  list_display = ('id', 'release_date', 'pass_fail_criteria', 'market')
  search_fields = ['id', 'release_date', 'pass_fail_criteria', 'market']
admin.site.register(Release, ReleaseAdmin)

class RiskAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'description', 'probability', 'severity', 'status')
  search_fields = ['id', 'title', 'description', 'category', 'probability', 'severity', 'status']
admin.site.register(Risk, RiskAdmin)

class TeamAdmin(admin.ModelAdmin):
  list_display = ('id', 'name')
  search_fields = ['id', 'name']
admin.site.register(Team, TeamAdmin)

class MemberAdmin(admin.ModelAdmin):
  list_display = ('id', 'first_name', 'last_name', 'title', 'is_manager')
  search_fields = ['id', 'first_name', 'last_name','title', 'is_manager']
admin.site.register(Member, MemberAdmin)

class MilestoneAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'description', 'start_date', 'percent_complete')
  search_fields = ['id', 'title', 'description', 'category', 'start_date', 'percent_complete']
admin.site.register(Milestone, MilestoneAdmin)

class RoadmapAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'description', 'end_date', 'market')
  search_fields = ['id', 'title', 'description', 'category', 'end_date', 'market']
admin.site.register(Roadmap, RoadmapAdmin)



