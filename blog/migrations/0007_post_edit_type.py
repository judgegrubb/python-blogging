# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='edit_type',
            field=models.CharField(default=b'M', max_length=1, choices=[(b'M', b'Markdown'), (b'H', b'HTML')]),
        ),
    ]
