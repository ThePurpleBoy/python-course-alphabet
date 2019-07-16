# Generated by Django 2.2.2 on 2019-07-09 17:21

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20190709_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name=1),
        ),
        migrations.AlterField(
            model_name='comment',
            name='parent_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]