# Generated by Django 3.1.1 on 2020-09-10 20:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Date created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('name', models.CharField(max_length=256, unique=True, verbose_name='name')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
            ],
            options={
                'verbose_name': 'Program',
                'verbose_name_plural': 'Programs',
            },
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Date created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('value', models.IntegerField(choices=[(1, 'Very bad'), (2, 'Bad'), (3, 'Normal'), (4, 'Good'), (5, 'Excellent')], verbose_name='Value')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='journal.program', verbose_name='Program')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Student')),
            ],
            options={
                'verbose_name': 'Journal',
                'verbose_name_plural': 'Journals',
            },
        ),
    ]
