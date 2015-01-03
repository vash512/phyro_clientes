# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Cliente'
        db.create_table(u'clientes_cliente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
            ('direccion', self.gf('django.db.models.fields.TextField')()),
            ('correo', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('twitter', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('facebook', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'clientes', ['Cliente'])

        # Adding M2M table for field preferencias on 'Cliente'
        m2m_table_name = db.shorten_name(u'clientes_cliente_preferencias')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('cliente', models.ForeignKey(orm[u'clientes.cliente'], null=False)),
            ('preferencia', models.ForeignKey(orm[u'clientes.preferencia'], null=False))
        ))
        db.create_unique(m2m_table_name, ['cliente_id', 'preferencia_id'])

        # Adding model 'Telefono'
        db.create_table(u'clientes_telefono', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clientes.Cliente'])),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=245, null=True, blank=True)),
        ))
        db.send_create_signal(u'clientes', ['Telefono'])

        # Adding model 'Proyecto'
        db.create_table(u'clientes_proyecto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('eslogan', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
            ('mantra_interno', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('mantra_externo', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('imagen_corporativa', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('inicioD', self.gf('django.db.models.fields.DateField')()),
            ('finalP', self.gf('django.db.models.fields.DateField')()),
            ('presupuesto', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'clientes', ['Proyecto'])

        # Adding M2M table for field requerimientos on 'Proyecto'
        m2m_table_name = db.shorten_name(u'clientes_proyecto_requerimientos')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('proyecto', models.ForeignKey(orm[u'clientes.proyecto'], null=False)),
            ('requerimiento', models.ForeignKey(orm[u'clientes.requerimiento'], null=False))
        ))
        db.create_unique(m2m_table_name, ['proyecto_id', 'requerimiento_id'])

        # Adding model 'Etapa'
        db.create_table(u'clientes_etapa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('proyecto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clientes.Proyecto'])),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=245)),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
            ('nivel', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'clientes', ['Etapa'])

        # Adding model 'RequerimientoUsuario'
        db.create_table(u'clientes_requerimientousuario', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('etapa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clientes.Etapa'])),
            ('requerimiento', self.gf('django.db.models.fields.TextField')()),
            ('realizado', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'clientes', ['RequerimientoUsuario'])

        # Adding model 'Tarea'
        db.create_table(u'clientes_tarea', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('etapa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clientes.Etapa'])),
            ('realizada', self.gf('django.db.models.fields.BooleanField')()),
            ('nivel', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('prioridad', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
            ('fechaTermino', self.gf('django.db.models.fields.DateField')()),
            ('resultados', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'clientes', ['Tarea'])

        # Adding model 'Preferencia'
        db.create_table(u'clientes_preferencia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('preferencia', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'clientes', ['Preferencia'])

        # Adding model 'Requerimiento'
        db.create_table(u'clientes_requerimiento', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('requerimiento', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'clientes', ['Requerimiento'])


    def backwards(self, orm):
        # Deleting model 'Cliente'
        db.delete_table(u'clientes_cliente')

        # Removing M2M table for field preferencias on 'Cliente'
        db.delete_table(db.shorten_name(u'clientes_cliente_preferencias'))

        # Deleting model 'Telefono'
        db.delete_table(u'clientes_telefono')

        # Deleting model 'Proyecto'
        db.delete_table(u'clientes_proyecto')

        # Removing M2M table for field requerimientos on 'Proyecto'
        db.delete_table(db.shorten_name(u'clientes_proyecto_requerimientos'))

        # Deleting model 'Etapa'
        db.delete_table(u'clientes_etapa')

        # Deleting model 'RequerimientoUsuario'
        db.delete_table(u'clientes_requerimientousuario')

        # Deleting model 'Tarea'
        db.delete_table(u'clientes_tarea')

        # Deleting model 'Preferencia'
        db.delete_table(u'clientes_preferencia')

        # Deleting model 'Requerimiento'
        db.delete_table(u'clientes_requerimiento')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'clientes.cliente': {
            'Meta': {'object_name': 'Cliente'},
            'correo': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'direccion': ('django.db.models.fields.TextField', [], {}),
            'facebook': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'preferencias': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['clientes.Preferencia']", 'symmetrical': 'False'}),
            'twitter': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'clientes.etapa': {
            'Meta': {'object_name': 'Etapa'},
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nivel': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'proyecto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.Proyecto']"}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '245'})
        },
        u'clientes.preferencia': {
            'Meta': {'object_name': 'Preferencia'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'preferencia': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'clientes.proyecto': {
            'Meta': {'object_name': 'Proyecto'},
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'eslogan': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'finalP': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen_corporativa': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'inicioD': ('django.db.models.fields.DateField', [], {}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'mantra_externo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mantra_interno': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'presupuesto': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'requerimientos': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['clientes.Requerimiento']", 'symmetrical': 'False'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'clientes.requerimiento': {
            'Meta': {'object_name': 'Requerimiento'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'requerimiento': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'clientes.requerimientousuario': {
            'Meta': {'object_name': 'RequerimientoUsuario'},
            'etapa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.Etapa']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'realizado': ('django.db.models.fields.BooleanField', [], {}),
            'requerimiento': ('django.db.models.fields.TextField', [], {})
        },
        u'clientes.tarea': {
            'Meta': {'object_name': 'Tarea'},
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'etapa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.Etapa']"}),
            'fechaTermino': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nivel': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'prioridad': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'realizada': ('django.db.models.fields.BooleanField', [], {}),
            'resultados': ('django.db.models.fields.TextField', [], {})
        },
        u'clientes.telefono': {
            'Meta': {'object_name': 'Telefono'},
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.Cliente']"}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '245', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['clientes']