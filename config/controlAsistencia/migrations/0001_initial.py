# -*- coding: utf-8 -*-
<<<<<<< HEAD
# Generated by Django 1.11.16 on 2018-10-23 13:04
=======
<<<<<<< HEAD
# Generated by Django 1.10.6 on 2018-10-23 13:04
=======
# Generated by Django 1.11.6 on 2018-10-23 12:59
>>>>>>> 6bbbbdd9ccfda91fc68e044079bc9ea7efaf800d
>>>>>>> 15b63cacc1e6eb231d58ad1eb876859d1712a494
from __future__ import unicode_literals

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
            name='Absence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('percentage', models.FloatField(choices=[(0.25, '1/4'), (0.5, '1/2'), (0.75, '3/4'), (1.0, '1')])),
                ('origin', models.IntegerField(choices=[(0, 'Falta'), (1, 'Llegada tarde'), (2, 'Retiro anticipado')])),
                ('justified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.IntegerField()),
                ('address', models.CharField(max_length=50)),
                ('neighbourhood', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Preceptor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internal_tel', models.PositiveIntegerField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('dni', models.PositiveIntegerField()),
                ('student_tag', models.PositiveIntegerField()),
                ('list_number', models.PositiveIntegerField()),
                ('birthday', models.DateField()),
                ('address', models.CharField(max_length=50)),
                ('neighbourhood', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('1', 'REGULAR'), ('2', 'PRIMERA REINCORPORACION'), ('3', 'SEGUNDA REINCORPORACION'), ('4', 'LIBRE')], max_length=1)),
                ('food_obvs', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_number', models.IntegerField(choices=[(1, 'Primero'), (2, 'Segundo'), (3, 'Tercero'), (4, 'Cuarto'), (5, 'Quinto'), (6, 'Sexto'), (7, 'Septimo')])),
                ('division', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controlAsistencia.Year'),
        ),
        migrations.AddField(
            model_name='preceptor',
            name='year',
            field=models.ManyToManyField(blank=True, related_name='preceptores', to='controlAsistencia.Year'),
        ),
        migrations.AddField(
            model_name='parent',
            name='childs',
            field=models.ManyToManyField(related_name='parents', to='controlAsistencia.Student'),
        ),
        migrations.AddField(
            model_name='parent',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='absence',
            name='preceptor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controlAsistencia.Preceptor'),
        ),
        migrations.AddField(
            model_name='absence',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controlAsistencia.Student'),
        ),
        migrations.AddField(
            model_name='absence',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controlAsistencia.Year'),
        ),
    ]
