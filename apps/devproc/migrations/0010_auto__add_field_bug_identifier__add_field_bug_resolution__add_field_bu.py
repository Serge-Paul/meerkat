# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Bug.identifier'
        db.add_column('devproc_bug', 'identifier', self.gf('django.db.models.fields.CharField')(default=-1, max_length=200), keep_default=False)

        # Adding field 'Bug.resolution'
        db.add_column('devproc_bug', 'resolution', self.gf('django.db.models.fields.TextField')(max_length=1028, null=True, blank=True), keep_default=False)

        # Adding field 'Bug.betatest'
        db.add_column('devproc_bug', 'betatest', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['devproc.BetaTest'], null=True, blank=True), keep_default=False)

        # Adding M2M table for field category on 'Bug'
        db.create_table('devproc_bug_category', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('bug', models.ForeignKey(orm['devproc.bug'], null=False)),
            ('category', models.ForeignKey(orm['devproc.category'], null=False))
        ))
        db.create_unique('devproc_bug_category', ['bug_id', 'category_id'])

        # Changing field 'Bug.description'
        db.alter_column('devproc_bug', 'description', self.gf('django.db.models.fields.TextField')(max_length=1028))

        # Deleting field 'Test.equipment'
        db.delete_column('devproc_test', 'equipment')

        # Deleting field 'Test.description'
        db.delete_column('devproc_test', 'description')

        # Adding field 'Test.test_description'
        db.add_column('devproc_test', 'test_description', self.gf('django.db.models.fields.TextField')(max_length=1028, null=True, blank=True), keep_default=False)

        # Adding field 'Test.implementation_description'
        db.add_column('devproc_test', 'implementation_description', self.gf('django.db.models.fields.TextField')(max_length=1028, null=True, blank=True), keep_default=False)

        # Adding field 'Test.identifier'
        db.add_column('devproc_test', 'identifier', self.gf('django.db.models.fields.CharField')(default=-1, max_length=200), keep_default=False)

        # Deleting field 'Feature.description'
        db.delete_column('devproc_feature', 'description')

        # Adding field 'Feature.design_description'
        db.add_column('devproc_feature', 'design_description', self.gf('django.db.models.fields.TextField')(default=-1, max_length=1028), keep_default=False)

        # Adding field 'Feature.implementation_description'
        db.add_column('devproc_feature', 'implementation_description', self.gf('django.db.models.fields.TextField')(default=-1, max_length=1028), keep_default=False)

        # Adding field 'Feature.identifier'
        db.add_column('devproc_feature', 'identifier', self.gf('django.db.models.fields.CharField')(default=-1, max_length=200), keep_default=False)

        # Adding field 'Feature.notes'
        db.add_column('devproc_feature', 'notes', self.gf('django.db.models.fields.TextField')(max_length=1028, null=True, blank=True), keep_default=False)

        # Adding M2M table for field component on 'Feature'
        db.create_table('devproc_feature_component', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('feature', models.ForeignKey(orm['devproc.feature'], null=False)),
            ('component', models.ForeignKey(orm['devproc.component'], null=False))
        ))
        db.create_unique('devproc_feature_component', ['feature_id', 'component_id'])


    def backwards(self, orm):
        
        # Deleting field 'Bug.identifier'
        db.delete_column('devproc_bug', 'identifier')

        # Deleting field 'Bug.resolution'
        db.delete_column('devproc_bug', 'resolution')

        # Deleting field 'Bug.betatest'
        db.delete_column('devproc_bug', 'betatest_id')

        # Removing M2M table for field category on 'Bug'
        db.delete_table('devproc_bug_category')

        # Changing field 'Bug.description'
        db.alter_column('devproc_bug', 'description', self.gf('django.db.models.fields.CharField')(max_length=1028))

        # Adding field 'Test.equipment'
        db.add_column('devproc_test', 'equipment', self.gf('django.db.models.fields.CharField')(max_length=1028, null=True, blank=True), keep_default=False)

        # Adding field 'Test.description'
        db.add_column('devproc_test', 'description', self.gf('django.db.models.fields.CharField')(default=-1, max_length=1028), keep_default=False)

        # Deleting field 'Test.test_description'
        db.delete_column('devproc_test', 'test_description')

        # Deleting field 'Test.implementation_description'
        db.delete_column('devproc_test', 'implementation_description')

        # Deleting field 'Test.identifier'
        db.delete_column('devproc_test', 'identifier')

        # Adding field 'Feature.description'
        db.add_column('devproc_feature', 'description', self.gf('django.db.models.fields.CharField')(default=-1, max_length=1028), keep_default=False)

        # Deleting field 'Feature.design_description'
        db.delete_column('devproc_feature', 'design_description')

        # Deleting field 'Feature.implementation_description'
        db.delete_column('devproc_feature', 'implementation_description')

        # Deleting field 'Feature.identifier'
        db.delete_column('devproc_feature', 'identifier')

        # Deleting field 'Feature.notes'
        db.delete_column('devproc_feature', 'notes')

        # Removing M2M table for field component on 'Feature'
        db.delete_table('devproc_feature_component')


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
            'features': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['devproc.Feature']", 'null': 'True', 'blank': 'True'}),
            'feedback': ('django.db.models.fields.CharField', [], {'max_length': '1028'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'release': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['devproc.Release']", 'unique': 'True'})
        },
        'devproc.bug': {
            'Meta': {'object_name': 'Bug'},
            'betatest': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devproc.BetaTest']", 'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['devproc.Category']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '1028'}),
            'features': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['devproc.Feature']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'release': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devproc.Release']", 'null': 'True', 'blank': 'True'}),
            'resolution': ('django.db.models.fields.TextField', [], {'max_length': '1028', 'null': 'True', 'blank': 'True'}),
            'severity': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'test': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devproc.Test']", 'null': 'True', 'blank': 'True'}),
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
            'attributes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['devproc.Attribute']", 'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['devproc.Category']", 'null': 'True', 'blank': 'True'}),
            'design_description': ('django.db.models.fields.TextField', [], {'max_length': '1028'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'implementation_description': ('django.db.models.fields.TextField', [], {'max_length': '1028'}),
            'notes': ('django.db.models.fields.TextField', [], {'max_length': '1028', 'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devproc.Component']", 'null': 'True', 'blank': 'True'}),
            'release': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devproc.Release']", 'null': 'True', 'blank': 'True'}),
            'requirements': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['devproc.Requirement']", 'null': 'True', 'blank': 'True'}),
            'responsible_engineer': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['devproc.Member']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'usecases': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['devproc.UseCase']", 'null': 'True', 'blank': 'True'})
        },
        'devproc.customer': {
            'Meta': {'object_name': 'Customer'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'devproc.feature': {
            'Meta': {'object_name': 'Feature'},
            'approval_status': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['devproc.Category']", 'null': 'True', 'blank': 'True'}),
            'component': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['devproc.Component']", 'null': 'True', 'blank': 'True'}),
            'design_description': ('django.db.models.fields.TextField', [], {'max_length': '1028'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'implementation_description': ('django.db.models.fields.TextField', [], {'max_length': '1028'}),
            'notes': ('django.db.models.fields.TextField', [], {'max_length': '1028', 'null': 'True', 'blank': 'True'}),
            'release': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devproc.Release']", 'null': 'True', 'blank': 'True'}),
            'requirements': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['devproc.Requirement']", 'null': 'True', 'blank': 'True'}),
            'responsible_engineer': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['devproc.Member']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'usecases': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['devproc.UseCase']", 'null': 'True', 'blank': 'True'})
        },
        'devproc.member': {
            'Meta': {'object_name': 'Member'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_manager': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devproc.Team']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'devproc.milestone': {
            'Meta': {'object_name': 'Milestone'},
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['devproc.Category']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'percent_complete': ('django.db.models.fields.IntegerField', [], {}),
            'release': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devproc.Release']"}),
            'roadmap': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devproc.Roadmap']", 'null': 'True', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'successors': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['devproc.Milestone']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'devproc.release': {
            'Meta': {'object_name': 'Release'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'market': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pass_fail_criteria': ('django.db.models.fields.CharField', [], {'max_length': '1028', 'null': 'True', 'blank': 'True'}),
            'release_date': ('django.db.models.fields.DateTimeField', [], {}),
            'roadmap': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devproc.Roadmap']", 'null': 'True', 'blank': 'True'})
        },
        'devproc.requirement': {
            'Meta': {'object_name': 'Requirement'},
            'approval_status': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['devproc.Category']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1028'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'notes': ('django.db.models.fields.TextField', [], {'max_length': '1028', 'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devproc.Requirement']", 'null': 'True', 'blank': 'True'}),
            'priority': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'release': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devproc.Release']", 'null': 'True', 'blank': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'use_case': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devproc.UseCase']", 'null': 'True', 'blank': 'True'})
        },
        'devproc.risk': {
            'Meta': {'object_name': 'Risk'},
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['devproc.Category']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'features': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['devproc.Feature']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'probability': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'release': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devproc.Release']", 'null': 'True', 'blank': 'True'}),
            'severity': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'devproc.roadmap': {
            'Meta': {'object_name': 'Roadmap'},
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['devproc.Category']", 'null': 'True', 'blank': 'True'}),
            'customers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['devproc.Customer']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'features': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['devproc.Feature']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'market': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'devproc.team': {
            'Meta': {'object_name': 'Team'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'devproc.test': {
            'Meta': {'object_name': 'Test'},
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['devproc.Category']", 'null': 'True', 'blank': 'True'}),
            'features': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['devproc.Feature']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'implementation_description': ('django.db.models.fields.TextField', [], {'max_length': '1028', 'null': 'True', 'blank': 'True'}),
            'pass_fail_criteria': ('django.db.models.fields.CharField', [], {'max_length': '1028', 'null': 'True', 'blank': 'True'}),
            'responsible_engineer': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['devproc.Member']", 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'test_description': ('django.db.models.fields.TextField', [], {'max_length': '1028', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'devproc.usecase': {
            'Meta': {'object_name': 'UseCase'},
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['devproc.Category']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1028'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'notes': ('django.db.models.fields.TextField', [], {'max_length': '1028', 'null': 'True', 'blank': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'target_market': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['devproc']
