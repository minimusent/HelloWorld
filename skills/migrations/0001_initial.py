# Generated by Django 2.0.9 on 2018-12-23 21:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Benefit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Default', help_text='Enter benefit', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='JobRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter job title', max_length=20)),
                ('city', models.CharField(default='Los Angeles', max_length=30)),
                ('state', models.CharField(default='CA', max_length=2)),
                ('co_name', models.CharField(default='Google', max_length=30)),
                ('pos_type', models.CharField(default='Full Time', max_length=20)),
                ('low_salary', models.IntegerField()),
                ('high_salary', models.IntegerField()),
                ('typical_day', models.TextField(default='')),
                ('avg_day', models.TextField(default='')),
                ('tech_used', models.TextField(default='')),
                ('match', models.IntegerField(default='1')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('benefit', models.ManyToManyField(help_text='Select each benefit for this job.', to='skills.Benefit')),
                ('created_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Length',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length', models.IntegerField(help_text='months')),
            ],
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Required element.', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Default', help_text='Enter skill name', max_length=40)),
                ('length', models.ForeignKey(default='0', help_text='months', on_delete=django.db.models.deletion.CASCADE, to='skills.Length')),
            ],
        ),
        migrations.AddField(
            model_name='jobrecord',
            name='requirements',
            field=models.ManyToManyField(help_text='Select each requirement.', to='skills.Requirement'),
        ),
        migrations.AddField(
            model_name='jobrecord',
            name='skills',
            field=models.ManyToManyField(help_text='Select each skill.', to='skills.Skill'),
        ),
    ]
