
from south.db import db
from django.db import models
from palette.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Palette'
        db.create_table('palette_palette', (
            ('id', orm['palette.Palette:id']),
            ('title', orm['palette.Palette:title']),
            ('slug', orm['palette.Palette:slug']),
            ('description', orm['palette.Palette:description']),
        ))
        db.send_create_signal('palette', ['Palette'])
        
        # Adding model 'Colour'
        db.create_table('palette_colour', (
            ('id', orm['palette.Colour:id']),
            ('palette', orm['palette.Colour:palette']),
            ('title', orm['palette.Colour:title']),
            ('code', orm['palette.Colour:code']),
        ))
        db.send_create_signal('palette', ['Colour'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Palette'
        db.delete_table('palette_palette')
        
        # Deleting model 'Colour'
        db.delete_table('palette_colour')
        
    
    
    models = {
        'palette.colour': {
            'code': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'palette': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['palette.Palette']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'palette.palette': {
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django_extensions.db.models.AutoSlugField', ["_('slug')"], {'populate_from': "'title'"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }
    
    complete_apps = ['palette']
