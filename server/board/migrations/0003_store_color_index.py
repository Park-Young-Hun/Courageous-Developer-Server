# Generated by Django 3.2.6 on 2021-09-07 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_alter_store_biz_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='color_index',
            field=models.IntegerField(blank=True, db_column='color_index', null=True),
        ),
    ]
