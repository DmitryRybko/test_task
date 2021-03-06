# Generated by Django 4.0.6 on 2022-07-06 14:23

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Responsible',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.SmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('status', models.CharField(choices=[('created', 'created'), ('started', 'started'), ('stopped', 'stopped')], default='created', max_length=20)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('responsible', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.responsible')),
            ],
        ),
    ]
