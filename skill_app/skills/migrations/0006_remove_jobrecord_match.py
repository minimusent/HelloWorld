# Generated by Django 2.1.3 on 2018-12-16 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0005_auto_20181215_2021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobrecord',
            name='match',
        ),
    ]
