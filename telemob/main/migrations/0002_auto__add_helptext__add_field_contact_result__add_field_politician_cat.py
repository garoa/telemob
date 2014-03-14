# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HelpText'
        db.create_table(u'main_helptext', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('campaign', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Campaign'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('date_created', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('last_updated', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'main', ['HelpText'])

        # Adding field 'Contact.result'
        db.add_column(u'main_contact', 'result',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=10),
                      keep_default=False)

        # Adding field 'Politician.category'
        db.add_column(u'main_politician', 'category',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=20),
                      keep_default=False)

        # Adding field 'Politician.annex'
        db.add_column(u'main_politician', 'annex',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Politician.chamber'
        db.add_column(u'main_politician', 'chamber',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Politician.fax'
        db.add_column(u'main_politician', 'fax',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=20),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'HelpText'
        db.delete_table(u'main_helptext')

        # Deleting field 'Contact.result'
        db.delete_column(u'main_contact', 'result')

        # Deleting field 'Politician.category'
        db.delete_column(u'main_politician', 'category')

        # Deleting field 'Politician.annex'
        db.delete_column(u'main_politician', 'annex')

        # Deleting field 'Politician.chamber'
        db.delete_column(u'main_politician', 'chamber')

        # Deleting field 'Politician.fax'
        db.delete_column(u'main_politician', 'fax')


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
            'campaign': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['main.Campaign']", 'unique': 'True'}),
            'contacted_by': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'date_created': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'politician': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['main.Politician']", 'unique': 'True'}),
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