# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Politician.parliamentary_name'
        db.add_column(u'main_politician', 'parliamentary_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=150),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Politician.parliamentary_name'
        db.delete_column(u'main_politician', 'parliamentary_name')


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
            'parliamentary_name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'political_party': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'tel': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'uf': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['main']