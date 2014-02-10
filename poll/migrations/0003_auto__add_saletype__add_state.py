# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Saletype'
        db.create_table(u'poll_saletype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=25)),
        ))
        db.send_create_signal(u'poll', ['Saletype'])

        # Adding model 'State'
        db.create_table(u'poll_state', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state_name', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('state_abbr', self.gf('django.db.models.fields.CharField')(max_length=5)),
        ))
        db.send_create_signal(u'poll', ['State'])


    def backwards(self, orm):
        # Deleting model 'Saletype'
        db.delete_table(u'poll_saletype')

        # Deleting model 'State'
        db.delete_table(u'poll_state')


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
            'designation': ('django.db.models.fields.CharField', [], {'default': "'Mr'", 'max_length': '5'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'poll.poll': {
            'Meta': {'object_name': 'Poll'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'poll.saletype': {
            'Meta': {'object_name': 'Saletype'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        u'poll.state': {
            'Meta': {'object_name': 'State'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state_abbr': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'state_name': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        }
    }

    complete_apps = ['poll']