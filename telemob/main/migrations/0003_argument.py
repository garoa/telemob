# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_campaign_template_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Argument',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(verbose_name='Texto do argumento')),
                ('campaign', models.ForeignKey(verbose_name='Campanha', to='main.Campaign')),
            ],
        ),
    ]
