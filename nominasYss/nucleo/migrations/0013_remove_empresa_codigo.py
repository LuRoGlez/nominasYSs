# Generated by Django 3.2 on 2021-08-04 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0012_auto_20210804_1020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresa',
            name='codigo',
        ),
    ]