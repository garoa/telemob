# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Contact', fields ['campaign']
        db.delete_unique(u'main_contact', ['campaign_id'])

        # Removing unique constraint on 'Contact', fields ['politician']
        db.delete_unique(u'main_contact', ['politician_id'])


        # Changing field 'Contact.politician'
        db.alter_column(u'main_contact', 'politician_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Politician']))

        # Changing field 'Contact.campaign'
        db.alter_column(u'main_contact', 'campaign_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Campaign']))

    def backwards(self, orm):

        # Changing field 'Contact.politician'
        db.alter_column(u'main_contact', 'politician_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['main.Politician'], unique=True))
        # Adding unique constraint on 'Contact', fields ['politician']
        db.create_unique(u'main_contact', ['politician_id'])


        # Changing field 'Contact.campaign'
        db.alter_column(u'main_contact', 'campaign_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['main.Campaign'], unique=True))
        # Adding unique constraint on 'Contact', fields ['campaign']
        db.create_unique(u'main_contact', ['campaign_id'])


    models = {
        u'main.campaign': {
            'Meta': {'object_name': 'Campaign'},
            'date_created': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'main.contact': {
            'Meta': {'object_name': 'Contact'},
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Campaign']"}),
            'contacted_by': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'date_created': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'politician': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Politician']"}),
            'result': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'main.helptext': {
            'Meta': {'object_name': 'HelpText'},
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Campaign']"}),
            'date_created': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'main.politician': {
            'Meta': {'object_name': 'Politician'},
            'annex': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'chamber': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '100'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'political_party': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'tel': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'uf': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['main']