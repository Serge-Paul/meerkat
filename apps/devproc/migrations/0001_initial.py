# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Category'
        db.create_table('devproc_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('devproc', ['Category'])

        # Adding model 'Requirement'
        db.create_table('devproc_requirement', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1028)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['devproc.Requirement'])),
            ('use_case', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['devproc.UseCase'], null=True, blank=True)),
            ('priority', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('release', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['devproc.Release'], null=True, blank=True)),
            ('approval_status', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('devproc', ['Requirement'])

        # Adding M2M table for field category on 'Requirement'
        db.create_table('devproc_requirement_category', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('requirement', models.ForeignKey(orm['devproc.requirement'], null=False)),
            ('category', models.ForeignKey(orm['devproc.category'], null=False))
        ))
        db.create_unique('devproc_requirement_category', ['requirement_id', 'category_id'])

        # Adding M2M table for field features on 'Requirement'
        db.create_table('devproc_requirement_features', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('requirement', models.ForeignKey(orm['devproc.requirement'], null=False)),
            ('feature', models.ForeignKey(orm['devproc.feature'], null=False))
        ))
        db.create_unique('devproc_requirement_features', ['requirement_id', 'feature_id'])

        # Adding M2M table for field tests on 'Requirement'
        db.create_table('devproc_requirement_tests', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('requirement', models.ForeignKey(orm['devproc.requirement'], null=False)),
            ('test', models.ForeignKey(orm['devproc.test'], null=False))
        ))
        db.create_unique('devproc_requirement_tests', ['requirement_id', 'test_id'])

        # Adding model 'UseCase'
        db.create_table('devproc_usecase', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1028)),
            ('target_market', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('target_user', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('release', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['devproc.Release'])),
        ))
        db.send_create_signal('devproc', ['UseCase'])

        # Adding M2M table for field category on 'UseCase'
        db.create_table('devproc_usecase_category', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('usecase', models.ForeignKey(orm['devproc.usecase'], null=False)),
            ('category', models.ForeignKey(orm['devproc.category'], null=False))
        ))
        db.create_unique('devproc_usecase_category', ['usecase_id', 'category_id'])

        # Adding M2M table for field features on 'UseCase'
        db.create_table('devproc_usecase_features', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('usecase', models.ForeignKey(orm['devproc.usecase'], null=False)),
            ('feature', models.ForeignKey(orm['devproc.feature'], null=False))
        ))
        db.create_unique('devproc_usecase_features', ['usecase_id', 'feature_id'])

        # Adding model 'Attribute'
        db.create_table('devproc_attribute', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1028)),
        ))
        db.send_create_signal('devproc', ['Attribute'])

        # Adding model 'Component'
        db.create_table('devproc_component', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1028)),
            ('attributes', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['devproc.Attribute'])),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['devproc.Component'])),
            ('release', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['devproc.Release'])),
            ('approval_status', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('devproc', ['Component'])

        # Adding M2M table for field responsible_engineer on 'Component'
        db.create_table('devproc_component_responsible_engineer', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('component', models.ForeignKey(orm['devproc.component'], null=False)),
            ('member', models.ForeignKey(orm['devproc.member'], null=False))
        ))
        db.create_unique('devproc_component_responsible_engineer', ['component_id', 'member_id'])

        # Adding M2M table for field category on 'Component'
        db.create_table('devproc_component_category', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('component', models.ForeignKey(orm['devproc.component'], null=False)),
            ('category', models.ForeignKey(orm['devproc.category'], null=False))
        ))
        db.create_unique('devproc_component_category', ['component_id', 'category_id'])

        # Adding model 'Feature'
        db.create_table('devproc_feature', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1028)),
            ('release', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['devproc.Release'])),
            ('approval_status', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('devproc', ['Feature'])

        # Adding M2M table for field category on 'Feature'
        db.create_table('devproc_feature_category', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('feature', models.ForeignKey(orm['devproc.feature'], null=False)),
            ('category', models.ForeignKey(orm['devproc.category'], null=False))
        ))
        db.create_unique('devproc_feature_category', ['feature_id', 'category_id'])

        # Adding M2M table for field responsible_engineer on 'Feature'
        db.create_table('devproc_feature_responsible_engineer', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('feature', models.ForeignKey(orm['devproc.feature'], null=False)),
            ('member', models.ForeignKey(orm['devproc.member'], null=False))
        ))
        db.create_unique('devproc_feature_responsible_engineer', ['feature_id', 'member_id'])

        # Adding model 'Test'
        db.create_table('devproc_test', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1028)),
            ('pass_fail_criteria', self.gf('django.db.models.fields.CharField')(max_length=1028)),
            ('equipment', self.gf('django.db.models.fields.CharField')(max_length=1028)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('devproc', ['Test'])

        # Adding M2M table for field category on 'Test'
        db.create_table('devproc_test_category', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('test', models.ForeignKey(orm['devproc.test'], null=False)),
            ('category', models.ForeignKey(orm['devproc.category'], null=False))
        ))
        db.create_unique('devproc_test_category', ['test_id', 'category_id'])

        # Adding M2M table for field features on 'Test'
        db.create_table('devproc_test_features', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('test', models.ForeignKey(orm['devproc.test'], null=False)),
            ('feature', models.ForeignKey(orm['devproc.feature'], null=False))
        ))
        db.create_unique('devproc_test_features', ['test_id', 'feature_id'])

        # Adding M2M table for field responsible_engineer on 'Test'
        db.create_table('devproc_test_responsible_engineer', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('test', models.ForeignKey(orm['devproc.test'], null=False)),
            ('member', models.ForeignKey(orm['devproc.member'], null=False))
        ))
        db.create_unique('devproc_test_responsible_engineer', ['test_id', 'member_id'])

        # Adding model 'Bug'
        db.create_table('devproc_bug', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1028)),
            ('severity', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('release', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['devproc.Test'])),
        ))
        db.send_create_signal('devproc', ['Bug'])

        # Adding M2M table for field features on 'Bug'
        db.create_table('devproc_bug_features', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('bug', models.ForeignKey(orm['devproc.bug'], null=False)),
            ('feature', models.ForeignKey(orm['devproc.feature'], null=False))
        ))
        db.create_unique('devproc_bug_features', ['bug_id', 'feature_id'])

        # Adding model 'BetaTest'
        db.create_table('devproc_betatest', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('release', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['devproc.Release'], unique=True)),
            ('feedback', self.gf('django.db.models.fields.CharField')(max_length=1028)),
        ))
        db.send_create_signal('devproc', ['BetaTest'])

        # Adding M2M table for field customer on 'BetaTest'
        db.create_table('devproc_betatest_customer', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('betatest', models.ForeignKey(orm['devproc.betatest'], null=False)),
            ('customer', models.ForeignKey(orm['devproc.customer'], null=False))
        ))
        db.create_unique('devproc_betatest_customer', ['betatest_id', 'customer_id'])

        # Adding M2M table for field features on 'BetaTest'
        db.create_table('devproc_betatest_features', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('betatest', models.ForeignKey(orm['devproc.betatest'], null=False)),
            ('feature', models.ForeignKey(orm['devproc.feature'], null=False))
        ))
        db.create_unique('devproc_betatest_features', ['betatest_id', 'feature_id'])

        # Adding model 'Customer'
        db.create_table('devproc_customer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('organization', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('devproc', ['Customer'])

        # Adding model 'Release'
        db.create_table('devproc_release', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('release_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('pass_fail_criteria', self.gf('django.db.models.fields.CharField')(max_length=1028)),
            ('market', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('roadmap', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['devproc.Roadmap'])),
        ))
        db.send_create_signal('devproc', ['Release'])

        # Adding model 'Risk'
        db.create_table('devproc_risk', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('release', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['devproc.Release'])),
            ('probability', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('severity', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('devproc', ['Risk'])

        # Adding M2M table for field category on 'Risk'
        db.create_table('devproc_risk_category', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('risk', models.ForeignKey(orm['devproc.risk'], null=False)),
            ('category', models.ForeignKey(orm['devproc.category'], null=False))
        ))
        db.create_unique('devproc_risk_category', ['risk_id', 'category_id'])

        # Adding M2M table for field features on 'Risk'
        db.create_table('devproc_risk_features', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('risk', models.ForeignKey(orm['devproc.risk'], null=False)),
            ('feature', models.ForeignKey(orm['devproc.feature'], null=False))
        ))
        db.create_unique('devproc_risk_features', ['risk_id', 'feature_id'])

        # Adding model 'Team'
        db.create_table('devproc_team', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('devproc', ['Team'])

        # Adding model 'Member'
        db.create_table('devproc_member', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['devproc.Team'])),
            ('is_manager', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('devproc', ['Member'])

        # Adding model 'Milestone'
        db.create_table('devproc_milestone', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('release', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['devproc.Release'])),
            ('percent_complete', self.gf('django.db.models.fields.IntegerField')()),
            ('roadmap', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['devproc.Roadmap'])),
        ))
        db.send_create_signal('devproc', ['Milestone'])

        # Adding M2M table for field category on 'Milestone'
        db.create_table('devproc_milestone_category', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('milestone', models.ForeignKey(orm['devproc.milestone'], null=False)),
            ('category', models.ForeignKey(orm['devproc.category'], null=False))
        ))
        db.create_unique('devproc_milestone_category', ['milestone_id', 'category_id'])

        # Adding M2M table for field successors on 'Milestone'
        db.create_table('devproc_milestone_successors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_milestone', models.ForeignKey(orm['devproc.milestone'], null=False)),
            ('to_milestone', models.ForeignKey(orm['devproc.milestone'], null=False))
        ))
        db.create_unique('devproc_milestone_successors', ['from_milestone_id', 'to_milestone_id'])

        # Adding model 'Roadmap'
        db.create_table('devproc_roadmap', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('market', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('devproc', ['Roadmap'])

        # Adding M2M table for field category on 'Roadmap'
        db.create_table('devproc_roadmap_category', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('roadmap', models.ForeignKey(orm['devproc.roadmap'], null=False)),
            ('category', models.ForeignKey(orm['devproc.category'], null=False))
        ))
        db.create_unique('devproc_roadmap_category', ['roadmap_id', 'category_id'])

        # Adding M2M table for field features on 'Roadmap'
        db.create_table('devproc_roadmap_features', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('roadmap', models.ForeignKey(orm['devproc.roadmap'], null=False)),
            ('feature', models.ForeignKey(orm['devproc.feature'], null=False))
        ))
        db.create_unique('devproc_roadmap_features', ['roadmap_id', 'feature_id'])

        # Adding M2M table for field customers on 'Roadmap'
        db.create_table('devproc_roadmap_customers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('roadmap', models.ForeignKey(orm['devproc.roadmap'], null=False)),
            ('customer', models.ForeignKey(orm['devproc.customer'], null=False))
        ))
        db.create_unique('devproc_roadmap_customers', ['roadmap_id', 'customer_id'])


    def backwards(self, orm):
        
        # Deleting model 'Category'
        db.delete_table('devproc_category')

        # Deleting model 'Requirement'
        db.delete_table('devproc_requirement')

        # Removing M2M table for field category on 'Requirement'
        db.delete_table('devproc_requirement_category')

        # Removing M2M table for field features on 'Requirement'
        db.delete_table('devproc_requirement_features')

        # Removing M2M table for field tests on 'Requirement'
        db.delete_table('devproc_requirement_tests')

        # Deleting model 'UseCase'
        db.delete_table('devproc_usecase')

        # Removing M2M table for field category on 'UseCase'
        db.delete_table('devproc_usecase_category')

        # Removing M2M table for field features on 'UseCase'
        db.delete_table('devproc_usecase_features')

        # Deleting model 'Attribute'
        db.delete_table('devproc_attribute')

        # Deleting model 'Component'
        db.delete_table('devproc_component')

        # Removing M2M table for field responsible_engineer on 'Component'
        db.delete_table('devproc_component_responsible_engineer')

        # Removing M2M table for field category on 'Component'
        db.delete_table('devproc_component_category')

        # Deleting model 'Feature'
        db.delete_table('devproc_feature')

        # Removing M2M table for field category on 'Feature'
        db.delete_table('devproc_feature_category')

        # Removing M2M table for field responsible_engineer on 'Feature'
        db.delete_table('devproc_feature_responsible_engineer')

        # Deleting model 'Test'
        db.delete_table('devproc_test')

        # Removing M2M table for field category on 'Test'
        db.delete_table('devproc_test_category')

        # Removing M2M table for field features on 'Test'
        db.delete_table('devproc_test_features')

        # Removing M2M table for field responsible_engineer on 'Test'
        db.delete_table('devproc_test_responsible_engineer')

        # Deleting model 'Bug'
        db.delete_table('devproc_bug')

        # Removing M2M table for field features on 'Bug'
        db.delete_table('devproc_bug_features')

        # Deleting model 'BetaTest'
        db.delete_table('devproc_betatest')

        # Removing M2M table for field customer on 'BetaTest'
        db.delete_table('devproc_betatest_customer')

        # Removing M2M table for field features on 'BetaTest'
        db.delete_table('devproc_betatest_features')

        # Deleting model 'Customer'
        db.delete_table('devproc_customer')

        # Deleting model 'Release'
        db.delete_table('devproc_release')

        # Deleting model 'Risk'
        db.delete_table('devproc_risk')

        # Removing M2M table for field category on 'Risk'
        db.delete_table('devproc_risk_category')

        # Removing M2M table for field features on 'Risk'
        db.delete_table('devproc_risk_features')

        # Deleting model 'Team'
        db.delete_table('devproc_team')

        # Deleting model 'Member'
        db.delete_table('devproc_member')

        # Deleting model 'Milestone'
        db.delete_table('devproc_milestone')

        # Removing M2M table for field category on 'Milestone'
        db.delete_table('devproc_milestone_category')

        # Removing M2M table for field successors on 'Milestone'
        db.delete_table('devproc_milestone_successors')

        # Deleting model 'Roadmap'
        db.delete_table('devproc_roadmap')

        # Removing M2M table for field category on 'Roadmap'
        db.delete_table('devproc_roadmap_category')

        # Removing M2M table for field features on 'Roadmap'
        db.delete_table('devproc_roadmap_features')

        # Removing M2M table for field customers on 'Roadmap'
        db.delete_table('devproc_roadmap_customers')


    models = {
        'devproc.attribute': {
            'Meta': {'object_name': 'Attribute'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1028'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'devproc.betatest': {
            'Meta': {'object_name': 'BetaTest'},
            'customer': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['devproc.Customer']", 'symmetrical': 'False'}),
            'features': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['devproc.Feature']", 'symmetrical': 'False'}),
            'feedback': ('django.db.models.fields.CharField', [], {'max_length': '1028'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'release': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['devproc.Release']", 'unique': 'True'})
        },
        'devproc.bug': {
            'Meta': {'object_name': 'Bug'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1028'}),
            'features': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['devproc.Feature']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'release': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devproc.Test']"}),
            'severity': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'devproc.category': {
            'Meta': {'object_name': 'Category'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'devproc.component': {
            'Meta': {'object_name': 'Component'},
            'approval_status': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'attributes': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devproc.Attribute']"}),
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['devproc.Category']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1028'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devproc.Component']"}),
            'release': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devproc.Release']"}),
            'responsible_engineer': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['devproc.Member']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'devproc.customer': {
            'Meta': {'object_name': 'Customer'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'devproc.feature': {
            'Meta': {'object_name': 'Feature'},
            'approval_status': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['devproc.Category']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1028'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'release': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devproc.Release']"}),
            'responsible_engineer': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['devproc.Member']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'devproc.member': {
            'Meta': {'object_name': 'Member'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_manager': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devproc.Team']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'devproc.milestone': {
            'Meta': {'object_name': 'Milestone'},
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['devproc.Category']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'percent_complete': ('django.db.models.fields.IntegerField', [], {}),
            'release': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devproc.Release']"}),
            'roadmap': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devproc.Roadmap']"}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'successors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['devproc.Milestone']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'devproc.release': {
            'Meta': {'object_name': 'Release'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'market': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pass_fail_criteria': ('django.db.models.fields.CharField', [], {'max_length': '1028'}),
            'release_date': ('django.db.models.fields.DateTimeField', [], {}),
            'roadmap': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devproc.Roadmap']"})
        },
        'devproc.requirement': {
            'Meta': {'object_name': 'Requirement'},
            'approval_status': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['devproc.Category']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1028'}),
            'features': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['devproc.Feature']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devproc.Requirement']"}),
            'priority': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'release': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devproc.Release']", 'null': 'True', 'blank': 'True'}),
            'tests': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['devproc.Test']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'use_case': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devproc.UseCase']", 'null': 'True', 'blank': 'True'})
        },
        'devproc.risk': {
            'Meta': {'object_name': 'Risk'},
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['devproc.Category']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'features': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['devproc.Feature']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'probability': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'release': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devproc.Release']"}),
            'severity': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'devproc.roadmap': {
            'Meta': {'object_name': 'Roadmap'},
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['devproc.Category']", 'symmetrical': 'False'}),
            'customers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['devproc.Customer']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'features': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['devproc.Feature']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'market': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'devproc.team': {
            'Meta': {'object_name': 'Team'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'devproc.test': {
            'Meta': {'object_name': 'Test'},
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['devproc.Category']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1028'}),
            'equipment': ('django.db.models.fields.CharField', [], {'max_length': '1028'}),
            'features': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['devproc.Feature']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pass_fail_criteria': ('django.db.models.fields.CharField', [], {'max_length': '1028'}),
            'responsible_engineer': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['devproc.Member']", 'symmetrical': 'False'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'devproc.usecase': {
            'Meta': {'object_name': 'UseCase'},
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['devproc.Category']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1028'}),
            'features': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['devproc.Feature']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'release': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devproc.Release']"}),
            'target_market': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'target_user': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['devproc']
