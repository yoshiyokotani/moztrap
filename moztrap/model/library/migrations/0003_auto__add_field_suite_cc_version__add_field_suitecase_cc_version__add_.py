# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Adding field 'Suite.cc_version'
        db.add_column('library_suite', 'cc_version', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'SuiteCase.cc_version'
        db.add_column('library_suitecase', 'cc_version', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'CaseVersion.cc_version'
        db.add_column('library_caseversion', 'cc_version', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'CaseAttachment.cc_version'
        db.add_column('library_caseattachment', 'cc_version', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'Case.cc_version'
        db.add_column('library_case', 'cc_version', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'CaseStep.cc_version'
        db.add_column('library_casestep', 'cc_version', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)


    def backwards(self, orm):

        # Deleting field 'Suite.cc_version'
        db.delete_column('library_suite', 'cc_version')

        # Deleting field 'SuiteCase.cc_version'
        db.delete_column('library_suitecase', 'cc_version')

        # Deleting field 'CaseVersion.cc_version'
        db.delete_column('library_caseversion', 'cc_version')

        # Deleting field 'CaseAttachment.cc_version'
        db.delete_column('library_caseattachment', 'cc_version')

        # Deleting field 'Case.cc_version'
        db.delete_column('library_case', 'cc_version')

        # Deleting field 'CaseStep.cc_version'
        db.delete_column('library_casestep', 'cc_version')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.product': {
            'Meta': {'ordering': "['name']", 'object_name': 'Product'},
            'cc_version': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['auth.User']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 2, 25, 0, 1, 12, 190426)'}),
            'deleted_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['auth.User']"}),
            'deleted_on': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'has_team': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['auth.User']"}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 2, 25, 0, 1, 12, 190624)'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'own_team': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'core.productversion': {
            'Meta': {'ordering': "['product', 'order']", 'object_name': 'ProductVersion'},
            'cc_version': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['auth.User']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 2, 25, 0, 1, 12, 185878)'}),
            'deleted_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['auth.User']"}),
            'deleted_on': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'environments': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'productversion'", 'symmetrical': 'False', 'to': "orm['environments.Environment']"}),
            'has_team': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latest': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['auth.User']"}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 2, 25, 0, 1, 12, 186074)'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'own_team': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'symmetrical': 'False', 'blank': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'versions'", 'to': "orm['core.Product']"}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.user': {
            'Meta': {'object_name': 'User', 'db_table': "'auth_user'", '_ormbases': ['auth.User'], 'proxy': 'True'}
        },
        'environments.category': {
            'Meta': {'ordering': "['name']", 'object_name': 'Category'},
            'cc_version': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['auth.User']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 2, 25, 0, 1, 12, 196774)'}),
            'deleted_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['auth.User']"}),
            'deleted_on': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['auth.User']"}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 2, 25, 0, 1, 12, 196972)'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'environments.element': {
            'Meta': {'ordering': "['name']", 'object_name': 'Element'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'elements'", 'to': "orm['environments.Category']"}),
            'cc_version': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['auth.User']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 2, 25, 0, 1, 12, 189436)'}),
            'deleted_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['auth.User']"}),
            'deleted_on': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['auth.User']"}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 2, 25, 0, 1, 12, 189627)'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'environments.environment': {
            'Meta': {'object_name': 'Environment'},
            'cc_version': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['auth.User']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 2, 25, 0, 1, 12, 200292)'}),
            'deleted_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['auth.User']"}),
            'deleted_on': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'elements': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'environments'", 'symmetrical': 'False', 'to': "orm['environments.Element']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['auth.User']"}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 2, 25, 0, 1, 12, 200493)'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'environments'", 'null': 'True', 'to': "orm['environments.Profile']"})
        },
        'environments.profile': {
            'Meta': {'object_name': 'Profile'},
            'cc_version': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['auth.User']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 2, 25, 0, 1, 12, 197684)'}),
            'deleted_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['auth.User']"}),
            'deleted_on': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['auth.User']"}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 2, 25, 0, 1, 12, 197880)'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'library.case': {
            'Meta': {'object_name': 'Case'},
            'cc_version': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['auth.User']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 2, 25, 0, 1, 12, 192679)'}),
            'deleted_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['auth.User']"}),
            'deleted_on': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['auth.User']"}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 2, 25, 0, 1, 12, 192871)'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cases'", 'to': "orm['core.Product']"})
        },
        'library.caseattachment': {
            'Meta': {'object_name': 'CaseAttachment'},
            'attachment': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'caseversion': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'attachments'", 'to': "orm['library.CaseVersion']"}),
            'cc_version': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['auth.User']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 2, 25, 0, 1, 12, 187537)'}),
            'deleted_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['auth.User']"}),
            'deleted_on': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['auth.User']"}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 2, 25, 0, 1, 12, 187745)'})
        },
        'library.casestep': {
            'Meta': {'ordering': "['caseversion', 'number']", 'object_name': 'CaseStep'},
            'caseversion': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'steps'", 'to': "orm['library.CaseVersion']"}),
            'cc_version': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['auth.User']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 2, 25, 0, 1, 12, 191525)'}),
            'deleted_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['auth.User']"}),
            'deleted_on': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'expected': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instruction': ('django.db.models.fields.TextField', [], {}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['auth.User']"}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 2, 25, 0, 1, 12, 191712)'}),
            'number': ('django.db.models.fields.IntegerField', [], {})
        },
        'library.caseversion': {
            'Meta': {'ordering': "['case', 'productversion__order']", 'object_name': 'CaseVersion'},
            'case': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'versions'", 'to': "orm['library.Case']"}),
            'cc_version': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['auth.User']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 2, 25, 0, 1, 12, 198592)'}),
            'deleted_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['auth.User']"}),
            'deleted_on': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'environments': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'caseversion'", 'symmetrical': 'False', 'to': "orm['environments.Environment']"}),
            'envs_narrowed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latest': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['auth.User']"}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 2, 25, 0, 1, 12, 198795)'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'productversion': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'caseversions'", 'to': "orm['core.ProductVersion']"}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'draft'", 'max_length': '30', 'db_index': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'caseversions'", 'blank': 'True', 'to': "orm['tags.Tag']"})
        },
        'library.suite': {
            'Meta': {'object_name': 'Suite'},
            'cases': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'suites'", 'symmetrical': 'False', 'through': "orm['library.SuiteCase']", 'to': "orm['library.Case']"}),
            'cc_version': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['auth.User']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 2, 25, 0, 1, 12, 194131)'}),
            'deleted_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['auth.User']"}),
            'deleted_on': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['auth.User']"}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 2, 25, 0, 1, 12, 194340)'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'suites'", 'to': "orm['core.Product']"}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'draft'", 'max_length': '30', 'db_index': 'True'})
        },
        'library.suitecase': {
            'Meta': {'ordering': "['order']", 'object_name': 'SuiteCase'},
            'case': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'suitecases'", 'to': "orm['library.Case']"}),
            'cc_version': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['auth.User']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 2, 25, 0, 1, 12, 195643)'}),
            'deleted_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['auth.User']"}),
            'deleted_on': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['auth.User']"}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 2, 25, 0, 1, 12, 195852)'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'suite': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'suitecases'", 'to': "orm['library.Suite']"})
        },
        'tags.tag': {
            'Meta': {'object_name': 'Tag'},
            'cc_version': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['auth.User']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 2, 25, 0, 1, 12, 188495)'}),
            'deleted_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['auth.User']"}),
            'deleted_on': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['auth.User']"}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 2, 25, 0, 1, 12, 188686)'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Product']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['library']
