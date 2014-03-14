# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Campaign'
        db.create_table(u'main_campaign', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('date_created', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('last_updated', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'main', ['Campaign'])

        # Adding model 'Politician'
        db.create_table(u'main_politician', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('tel', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=100)),
            ('uf', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('political_party', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('date_created', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('last_updated', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'main', ['Politician'])

        # Adding model 'Contact'
        db.create_table(u'main_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('politician', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['main.Politician'], unique=True)),
            ('campaign', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['main.Campaign'], unique=True)),
            ('contacted_by', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('date_created', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'main', ['Contact'])


    def backwards(self, orm):
        # Deleting model 'Campaign'
        db.delete_table(u'main_campaign')

        # Deleting model 'Politician'
        db.delete_table(u'main_politician')

        # Deleting model 'Contact'
        db.delete_table(u'main_contact')


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
            'politician': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['main.Politician']", 'unique': 'True'})
        },
        u'main.politician': {
            'Meta': {'object_name': 'Politician'},
            'date_created': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'political_party': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'tel': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'uf': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['main']