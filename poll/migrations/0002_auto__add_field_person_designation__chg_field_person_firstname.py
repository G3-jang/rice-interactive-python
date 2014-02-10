# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Person.designation'
        db.add_column(u'poll_person', 'designation',
                      self.gf('django.db.models.fields.CharField')(default='Mr', max_length=5),
                      keep_default=False)


        # Changing field 'Person.firstname'
        db.alter_column(u'poll_person', 'firstname', self.gf('django.db.models.fields.CharField')(max_length=100))

    def backwards(self, orm):
        # Deleting field 'Person.designation'
        db.delete_column(u'poll_person', 'designation')


        # Changing field 'Person.firstname'
        db.alter_column(u'poll_person', 'firstname', self.gf('django.db.models.fields.CharField')(max_length=25))

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
        }
    }

    complete_apps = ['poll']