# Generated by Django 3.2 on 2021-08-02 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0003_auto_20210802_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelo111190',
            name='bases111',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='modelo111190',
            name='difBase',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='modelo111190',
            name='difReten',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='modelo111190',
            name='retenciones111',
            field=models.FloatField(blank=True, null=True),
        ),
    ]