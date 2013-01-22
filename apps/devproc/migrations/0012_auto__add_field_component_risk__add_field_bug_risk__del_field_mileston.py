# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Component.risk'
        db.add_column('devproc_component', 'risk', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['devproc.Risk'], unique=True, null=True, blank=True), keep_default=False)

        # Adding field 'Bug.risk'
        db.add_column('devproc_bug', 'risk', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['devproc.Risk'], unique=True, null=True, blank=True), keep_default=False)

        # Deleting field 'Milestone.roadmap'
        db.delete_column('devproc_milestone', 'roadmap_id')

        # Adding field 'Milestone.notes'
        db.add_column('devproc_milestone', 'notes', self.gf('django.db.models.fields.TextField')(max_length=1028, null=True, blank=True), keep_default=False)

        # Removing M2M table for field successors on 'Milestone'
        db.delete_table('devproc_milestone_successors')

        # Adding M2M table for field predecessors on 'Milestone'
        db.create_table('devproc_milestone_predecessors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_milestone', models.ForeignKey(orm['devproc.milestone'], null=False)),
            ('to_milestone', models.ForeignKey(orm['devproc.milestone'], null=False))
        ))
        db.create_unique('devproc_milestone_predecessors', ['from_milestone_id', 'to_milestone_id'])

        # Changing field 'Milestone.description'
        db.alter_column('devproc_milestone', 'description', self.gf('django.db.models.fields.TextField')(max_length=200))

        # Adding field 'Feature.risk'
        db.add_column('devproc_feature', 'risk', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['devproc.Risk'], unique=True, null=True, blank=True), keep_default=False)

        # Adding field 'Risk.identifier'
        db.add_column('devproc_risk', 'identifier', self.gf('django.db.models.fields.CharField')(default=-1, max_length=200), keep_default=False)

        # Adding field 'Risk.approval_status'
        db.add_column('devproc_risk', 'approval_status', self.gf('django.db.models.fields.CharField')(default=-1, max_length=128), keep_default=False)

        # Removing M2M table for field features on 'Risk'
        db.delete_table('devproc_risk_features')


    def backwards(self, orm):
        
        # Deleting field 'Component.risk'
        db.delete_column('devproc_component', 'risk_id')

        # Deleting field 'Bug.risk'
        db.delete_column('devproc_bug', 'risk_id')

        # Adding field 'Milestone.roadmap'
        db.add_column('devproc_milestone', 'roadmap', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['devproc.Roadmap'], null=True, blank=True), keep_default=False)

        # Deleting field 'Milestone.notes'
        db.delete_column('devproc_milestone', 'notes')

        # Adding M2M table for field successors on 'Milestone'
        db.create_table('devproc_milestone_successors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_milestone', models.ForeignKey(orm['devproc.milestone'], null=False)),
            ('to_milestone', models.ForeignKey(orm['devproc.milestone'], null=False))
        ))
        db.create_unique('devproc_milestone_successors', ['from_milestone_id', 'to_milestone_id'])

        # Removing M2M table for field predecessors on 'Milestone'
        db.delete_table('devproc_milestone_predecessors')

        # Changing field 'Milestone.description'
        db.alter_column('devproc_milestone', 'description', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Deleting field 'Feature.risk'
        db.delete_column('devproc_feature', 'risk_id')

        # Deleting field 'Risk.identifier'
        db.delete_column('devproc_risk', 'identifier')

        # Deleting field 'Risk.approval_status'
        db.delete_column('devproc_risk', 'approval_status')

        # Adding M2M table for field features on 'Risk'
        db.create_table('devproc_risk_features', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('risk', models.ForeignKey(orm['devproc.risk'], null=False)),
            ('feature', models.ForeignKey(orm['devproc.feature'], null=False))
        ))
        db.create_unique('devproc_risk_features', ['risk_id', 'feature_id'])


    models = {
        'devproc.attribute': {
            'Meta': {'object_name': 'Attribute'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1028'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'devproc.betatest': {
            'Meta': {'object_name': 'BetaTest'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'release': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['devproc.Release']", 'unique': 'True'}),
            'responsible_engineer': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['devproc.Member']", 'null': 'True', 'blank': 'True'})
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
            'risk': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['devproc.Risk']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
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
            'risk': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['devproc.Risk']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'usecases': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['devproc.UseCase']", 'null': 'True', 'blank': 'True'})
        },
        'devproc.customer': {
            'Meta': {'object_name': 'Customer'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
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
            'risk': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['devproc.Risk']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'usecases': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['devproc.UseCase']", 'null': 'True', 'blank': 'True'})
        },
        'devproc.feedback': {
            'Meta': {'object_name': 'Feedback'},
            'betatest': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devproc.BetaTest']"}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devproc.Customer']"}),
            'feature': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devproc.Feature']"}),
            'feedback': ('django.db.models.fields.TextField', [], {'max_length': '1028'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'devproc.member': {
            'Meta': {'object_name': 'Member'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_manager': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'team': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['devproc.Team']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'devproc.milestone': {
            'Meta': {'object_name': 'Milestone'},
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['devproc.Category']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'max_length': '1028', 'null': 'True', 'blank': 'True'}),
            'percent_complete': ('django.db.models.fields.IntegerField', [], {}),
            'predecessors': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['devproc.Milestone']", 'null': 'True', 'blank': 'True'}),
            'release': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devproc.Release']"}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'devproc.release': {
            'Meta': {'object_name': 'Release'},
            'goal': ('django.db.models.fields.CharField', [], {'max_length': '1028', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'market': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'notes': ('django.db.models.fields.TextField', [], {'max_length': '1028', 'null': 'True', 'blank': 'True'}),
            'pass_fail_criteria': ('django.db.models.fields.CharField', [], {'max_length': '1028', 'null': 'True', 'blank': 'True'}),
            'release_date': ('django.db.models.fields.DateTimeField', [], {}),
            'responsible_engineer': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['devproc.Member']", 'null': 'True', 'blank': 'True'}),
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
            'approval_status': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['devproc.Category']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
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
            'description': ('django.db.models.fields.TextField', [], {'max_length': '1028', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'responsibilities': ('django.db.models.fields.CharField', [], {'max_length': '128'})
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
