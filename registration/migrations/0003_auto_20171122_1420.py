# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20171115_1538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='picture',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='supervisor',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
