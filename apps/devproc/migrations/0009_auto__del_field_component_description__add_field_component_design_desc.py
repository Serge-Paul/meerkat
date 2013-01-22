# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Component.description'
        db.delete_column('devproc_component', 'description')

        # Adding field 'Component.design_description'
        db.add_column('devproc_component', 'design_description', self.gf('django.db.models.fields.TextField')(default=-1, max_length=1028), keep_default=False)

        # Adding field 'Component.implementation_description'
        db.add_column('devproc_component', 'implementation_description', self.gf('django.db.models.fields.TextField')(default=-1, max_length=1028), keep_default=False)

        # Adding field 'Component.identifier'
        db.add_column('devproc_component', 'identifier', self.gf('django.db.models.fields.CharField')(default=-1, max_length=200), keep_default=False)

        # Adding field 'Component.notes'
        db.add_column('devproc_component', 'notes', self.gf('django.db.models.fields.TextField')(max_length=1028, null=True, blank=True), keep_default=False)

        # Adding M2M table for field requirements on 'Component'
        db.create_table('devproc_component_requirements', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('component', models.ForeignKey(orm['devproc.component'], null=False)),
            ('requirement', models.ForeignKey(orm['devproc.requirement'], null=False))
        ))
        db.create_unique('devproc_component_requirements', ['component_id', 'requirement_id'])

        # Adding M2M table for field usecases on 'Component'
        db.create_table('devproc_component_usecases', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('component', models.ForeignKey(orm['devproc.component'], null=False)),
            ('usecase', models.ForeignKey(orm['devproc.usecase'], null=False))
        ))
        db.create_unique('devproc_component_usecases', ['component_id', 'usecase_id'])

        # Adding field 'Requirement.identifier'
        db.add_column('devproc_requirement', 'identifier', self.gf('django.db.models.fields.CharField')(default=-1, max_length=200), keep_default=False)

        # Adding field 'Requirement.source'
        db.add_column('devproc_requirement', 'source', self.gf('django.db.models.fields.CharField')(default=-1, max_length=128), keep_default=False)

        # Adding field 'Requirement.notes'
        db.add_column('devproc_requirement', 'notes', self.gf('django.db.models.fields.TextField')(max_length=1028, null=True, blank=True), keep_default=False)

        # Removing M2M table for field tests on 'Requirement'
        db.delete_table('devproc_requirement_tests')

        # Removing M2M table for field features on 'Requirement'
        db.delete_table('devproc_requirement_features')

        # Deleting field 'Feature.usecase'
        db.delete_column('devproc_feature', 'usecase_id')

        # Adding M2M table for field usecases on 'Feature'
        db.create_table('devproc_feature_usecases', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('feature', models.ForeignKey(orm['devproc.feature'], null=False)),
            ('usecase', models.ForeignKey(orm['devproc.usecase'], null=False))
        ))
        db.create_unique('devproc_feature_usecases', ['feature_id', 'usecase_id'])

        # Adding M2M table for field requirements on 'Feature'
        db.create_table('devproc_feature_requirements', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('feature', models.ForeignKey(orm['devproc.feature'], null=False)),
            ('requirement', models.ForeignKey(orm['devproc.requirement'], null=False))
        ))
        db.create_unique('devproc_feature_requirements', ['feature_id', 'requirement_id'])


    def backwards(self, orm):
        
        # Adding field 'Component.description'
        db.add_column('devproc_component', 'description', self.gf('django.db.models.fields.CharField')(default=-1, max_length=1028), keep_default=False)

        # Deleting field 'Component.design_description'
        db.delete_column('devproc_component', 'design_description')

        # Deleting field 'Component.implementation_description'
        db.delete_column('devproc_component', 'implementation_description')

        # Deleting field 'Component.identifier'
        db.delete_column('devproc_component', 'identifier')

        # Deleting field 'Component.notes'
        db.delete_column('devproc_component', 'notes')

        # Removing M2M table for field requirements on 'Component'
        db.delete_table('devproc_component_requirements')

        # Removing M2M table for field usecases on 'Component'
        db.delete_table('devproc_component_usecases')

        # Deleting field 'Requirement.identifier'
        db.delete_column('devproc_requirement', 'identifier')

        # Deleting field 'Requirement.source'
        db.delete_column('devproc_requirement', 'source')

        # Deleting field 'Requirement.notes'
        db.delete_column('devproc_requirement', 'notes')

        # Adding M2M table for field tests on 'Requirement'
        db.create_table('devproc_requirement_tests', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('requirement', models.ForeignKey(orm['devproc.requirement'], null=False)),
            ('test', models.ForeignKey(orm['devproc.test'], null=False))
        ))
        db.create_unique('devproc_requirement_tests', ['requirement_id', 'test_id'])

        # Adding M2M table for field features on 'Requirement'
        db.create_table('devproc_requirement_features', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('requirement', models.ForeignKey(orm['devproc.requirement'], null=False)),
            ('feature', models.ForeignKey(orm['devproc.feature'], null=False))
        ))
        db.create_unique('devproc_requirement_features', ['requirement_id', 'feature_id'])

        # Adding field 'Feature.usecase'
        db.add_column('devproc_feature', 'usecase', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['devproc.UseCase'], null=True, blank=True), keep_default=False)

        # Removing M2M table for field usecases on 'Feature'
        db.delete_table('devproc_feature_usecases')

        # Removing M2M table for field requirements on 'Feature'
        db.delete_table('devproc_feature_requirements')


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
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1028'}),
            'features': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['devproc.Feature']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'release': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devproc.Release']", 'null': 'True', 'blank': 'True'}),
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
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1028'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1028'}),
            'equipment': ('django.db.models.fields.CharField', [], {'max_length': '1028', 'null': 'True', 'blank': 'True'}),
            'features': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['devproc.Feature']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pass_fail_criteria': ('django.db.models.fields.CharField', [], {'max_length': '1028', 'null': 'True', 'blank': 'True'}),
            'responsible_engineer': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['devproc.Member']", 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
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
