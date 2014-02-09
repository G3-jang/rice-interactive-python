# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Person.saletype'
        db.add_column(u'poll_person', 'saletype',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['poll.Saletype'], null=True),
                      keep_default=False)

        # Adding field 'Person.loan_type'
        db.add_column(u'poll_person', 'loan_type',
                      self.gf('django.db.models.fields.CharField')(default='New', max_length=5),
                      keep_default=False)

        # Adding field 'Person.loan_amount'
        db.add_column(u'poll_person', 'loan_amount',
                      self.gf('django.db.models.fields.IntegerField')(default=5000),
                      keep_default=False)

        # Adding field 'Person.credit_tier'
        db.add_column(u'poll_person', 'credit_tier',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=700),
                      keep_default=False)

        # Adding field 'Person.street'
        db.add_column(u'poll_person', 'street',
                      self.gf('django.db.models.fields.CharField')(default='123', max_length=50),
                      keep_default=False)

        # Adding field 'Person.city'
        db.add_column(u'poll_person', 'city',
                      self.gf('django.db.models.fields.CharField')(default='fresno', max_length=20),
                      keep_default=False)

        # Adding field 'Person.state'
        db.add_column(u'poll_person', 'state',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['poll.State'], null=True),
                      keep_default=False)

        # Adding field 'Person.zipcode'
        db.add_column(u'poll_person', 'zipcode',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Person.saletype'
        db.delete_column(u'poll_person', 'saletype_id')

        # Deleting field 'Person.loan_type'
        db.delete_column(u'poll_person', 'loan_type')

        # Deleting field 'Person.loan_amount'
        db.delete_column(u'poll_person', 'loan_amount')

        # Deleting field 'Person.credit_tier'
        db.delete_column(u'poll_person', 'credit_tier')

        # Deleting field 'Person.street'
        db.delete_column(u'poll_person', 'street')

        # Deleting field 'Person.city'
        db.delete_column(u'poll_person', 'city')

        # Deleting field 'Person.state'
        db.delete_column(u'poll_person', 'state_id')

        # Deleting field 'Person.zipcode'
        db.delete_column(u'poll_person', 'zipcode')


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
            'city': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'credit_tier': ('django.db.models.fields.PositiveIntegerField', [], {'default': '700'}),
            'designation': ('django.db.models.fields.CharField', [], {'default': "'Mr'", 'max_length': '5'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'loan_amount': ('django.db.models.fields.IntegerField', [], {'default': '5000'}),
            'loan_type': ('django.db.models.fields.CharField', [], {'default': "'New'", 'max_length': '5'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'saletype': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['poll.Saletype']", 'null': 'True'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['poll.State']", 'null': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'zipcode': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
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