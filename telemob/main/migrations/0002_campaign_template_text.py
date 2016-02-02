# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='template_text',
            field=models.TextField(
                default=u'*** FORNEÇA UM TEXTO PARA TEMPLATE DA CAMPANHA ***',
                verbose_name='Template para telegrama, fax, email'),
            preserve_default=False,
        ),
    ]
