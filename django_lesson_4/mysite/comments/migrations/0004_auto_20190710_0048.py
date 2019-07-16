# Generated by Django 2.2.2 on 2019-07-09 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_auto_20190709_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='comment',
            name='parent_id',
            field=models.PositiveIntegerField(blank=True, default=None, null=True),
        ),
    ]