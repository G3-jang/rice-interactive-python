# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Poll'
        db.create_table(u'poll_poll', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'poll', ['Poll'])

        # Adding model 'Choice'
        db.create_table(u'poll_choice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('choice_text', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('poll', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['poll.Poll'])),
            ('votes', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'poll', ['Choice'])

        # Adding model 'Person'
        db.create_table(u'poll_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal(u'poll', ['Person'])


    def backwards(self, orm):
        # Deleting model 'Poll'
        db.delete_table(u'poll_poll')

        # Deleting model 'Choice'
        db.delete_table(u'poll_choice')

        # Deleting model 'Person'
        db.delete_table(u'poll_person')


    models = {
        u'poll.choice': {
            'Meta': {'object_name': 'Choice'},
            'choice_text': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'poll': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['poll.Poll']"}),
            'votes': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'poll.person': {
            'Meta': {'object_name': 'Person'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'poll.poll': {
            'Meta': {'object_name': 'Poll'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['poll']