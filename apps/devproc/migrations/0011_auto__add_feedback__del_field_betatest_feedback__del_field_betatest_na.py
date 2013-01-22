# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Feedback'
        db.create_table('devproc_feedback', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('betatest', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['devproc.BetaTest'])),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['devproc.Customer'])),
            ('feature', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['devproc.Feature'])),
            ('feedback', self.gf('django.db.models.fields.TextField')(max_length=1028)),
        ))
        db.send_create_signal('devproc', ['Feedback'])

        # Deleting field 'BetaTest.feedback'
        db.delete_column('devproc_betatest', 'feedback')

        # Deleting field 'BetaTest.name'
        db.delete_column('devproc_betatest', 'name')

        # Removing M2M table for field customer on 'BetaTest'
        db.delete_table('devproc_betatest_customer')

        # Removing M2M table for field features on 'BetaTest'
        db.delete_table('devproc_betatest_features')

        # Adding M2M table for field responsible_engineer on 'BetaTest'
        db.create_table('devproc_betatest_responsible_engineer', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('betatest', models.ForeignKey(orm['devproc.betatest'], null=False)),
            ('member', models.ForeignKey(orm['devproc.member'], null=False))
        ))
        db.create_unique('devproc_betatest_responsible_engineer', ['betatest_id', 'member_id'])

        # Adding field 'Release.notes'
        db.add_column('devproc_release', 'notes', self.gf('django.db.models.fields.TextField')(max_length=1028, null=True, blank=True), keep_default=False)

        # Adding field 'Release.goal'
        db.add_column('devproc_release', 'goal', self.gf('django.db.models.fields.CharField')(max_length=1028, null=True, blank=True), keep_default=False)

        # Adding M2M table for field responsible_engineer on 'Release'
        db.create_table('devproc_release_responsible_engineer', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('release', models.ForeignKey(orm['devproc.release'], null=False)),
            ('member', models.ForeignKey(orm['devproc.member'], null=False))
        ))
        db.create_unique('devproc_release_responsible_engineer', ['release_id', 'member_id'])

        # Adding field 'Team.description'
        db.add_column('devproc_team', 'description', self.gf('django.db.models.fields.TextField')(max_length=1028, null=True, blank=True), keep_default=False)

        # Adding field 'Team.responsibilities'
        db.add_column('devproc_team', 'responsibilities', self.gf('django.db.models.fields.CharField')(default=-1, max_length=128), keep_default=False)

        # Changing field 'Risk.description'
        db.alter_column('devproc_risk', 'description', self.gf('django.db.models.fields.TextField')(max_length=200))

        # Deleting field 'Member.team'
        db.delete_column('devproc_member', 'team_id')

        # Adding M2M table for field team on 'Member'
        db.create_table('devproc_member_team', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('member', models.ForeignKey(orm['devproc.member'], null=False)),
            ('team', models.ForeignKey(orm['devproc.team'], null=False))
        ))
        db.create_unique('devproc_member_team', ['member_id', 'team_id'])

        # Adding field 'Customer.location'
        db.add_column('devproc_customer', 'location', self.gf('django.db.models.fields.CharField')(default=-1, max_length=200), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'Feedback'
        db.delete_table('devproc_feedback')

        # Adding field 'BetaTest.feedback'
        db.add_column('devproc_betatest', 'feedback', self.gf('django.db.models.fields.CharField')(default=-1, max_length=1028), keep_default=False)

        # Adding field 'BetaTest.name'
        db.add_column('devproc_betatest', 'name', self.gf('django.db.models.fields.CharField')(default=-1, max_length=200), keep_default=False)

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

        # Removing M2M table for field responsible_engineer on 'BetaTest'
        db.delete_table('devproc_betatest_responsible_engineer')

        # Deleting field 'Release.notes'
        db.delete_column('devproc_release', 'notes')

        # Deleting field 'Release.goal'
        db.delete_column('devproc_release', 'goal')

        # Removing M2M table for field responsible_engineer on 'Release'
        db.delete_table('devproc_release_responsible_engineer')

        # Deleting field 'Team.description'
        db.delete_column('devproc_team', 'description')

        # Deleting field 'Team.responsibilities'
        db.delete_column('devproc_team', 'responsibilities')

        # Changing field 'Risk.description'
        db.alter_column('devproc_risk', 'description', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Adding field 'Member.team'
        db.add_column('devproc_member', 'team', self.gf('django.db.models.fields.related.ForeignKey')(default=-1, to=orm['devproc.Team']), keep_default=False)

        # Removing M2M table for field team on 'Member'
        db.delete_table('devproc_member_team')

        # Deleting field 'Customer.location'
        db.delete_column('devproc_customer', 'location')


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
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['devproc.Category']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
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
