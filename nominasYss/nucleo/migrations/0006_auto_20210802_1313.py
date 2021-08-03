# Generated by Django 3.2 on 2021-08-02 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0005_auto_20210802_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelo111190',
            name='base190',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='modelo111190',
            name='baseIRPF1T',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='modelo111190',
            name='baseIRPF2T',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='modelo111190',
            name='baseIRPF3T',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='modelo111190',
            name='baseIRPF4T',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='modelo111190',
            name='bases111',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='modelo111190',
            name='difBase',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='modelo111190',
            name='difReten',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='modelo111190',
            name='reten190',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='modelo111190',
            name='reten1T',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='modelo111190',
            name='reten2T',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='modelo111190',
            name='reten3T',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='modelo111190',
            name='reten4T',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='modelo111190',
            name='retenciones111',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
