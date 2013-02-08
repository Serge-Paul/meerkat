# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Milestone.description'
        db.alter_column('devproc_milestone', 'description', self.gf('django.db.models.fields.TextField')(max_length=1028))

        # Changing field 'Risk.description'
        db.alter_column('devproc_risk', 'description', self.gf('django.db.models.fields.TextField')(max_length=1028))


    def backwards(self, orm):
        
        # Changing field 'Milestone.description'
        db.alter_column('devproc_milestone', 'description', self.gf('django.db.models.fields.TextField')(max_length=200))

        # Changing field 'Risk.description'
        db.alter_column('devproc_risk', 'description', self.gf('django.db.models.fields.TextField')(max_length=200))


    models = {
        'devproc.attribute': {
            'Meta': {'object_name': 'Attribute'},
            'component': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devproc.Component']"}),
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
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '200'})
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
            'release': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devproc.Release']"}),
            'requirements': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['devproc.Requirement']", 'null': 'True', 'blank': 'True'}),
            'responsible_engineer': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['devproc.Member']", 'null': 'True', 'blank': 'True'}),
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
            'description': ('django.db.models.fields.TextField', [], {'max_length': '1028'}),
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
            'goals': ('django.db.models.fields.CharField', [], {'max_length': '1028', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'market': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'notes': ('django.db.models.fields.TextField', [], {'max_length': '1028', 'null': 'True', 'blank': 'True'}),
            'pass_fail_criteria': ('django.db.models.fields.CharField', [], {'max_length': '1028', 'null': 'True', 'blank': 'True'}),
            'release_date': ('django.db.models.fields.DateTimeField', [], {}),
            'responsible_engineer': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['devproc.Member']", 'null': 'True', 'blank': 'True'})
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
        'devproc.responsibility': {
            'Meta': {'object_name': 'Responsibility'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'release': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devproc.Release']"}),
            'responsibility': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devproc.Team']"})
        },
        'devproc.risk': {
            'Meta': {'object_name': 'Risk'},
            'approval_status': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'bug': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devproc.Bug']", 'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['devproc.Category']", 'null': 'True', 'blank': 'True'}),
            'component': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devproc.Component']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '1028'}),
            'feature': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devproc.Feature']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'probability': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'release': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devproc.Release']", 'null': 'True', 'blank': 'True'}),
            'severity': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'devproc.team': {
            'Meta': {'object_name': 'Team'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '1028', 'null': 'True', 'blank': 'True'}),
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
