# Generated by Django 5.0.6 on 2024-06-07 02:22

import django.db.models.deletion
from django.db import migrations, models

import thesis.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thesis',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('status', models.CharField(default='APPROVAL_PENDING', max_length=50, verbose_name=thesis.models.Thesis.ThesisStatus)),
                ('date_submitted', models.DateField(auto_now_add=True)),
                ('s3_url', models.URLField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.student')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('comments', models.TextField()),
                ('is_approved', models.BooleanField(default=False)),
                ('thesis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thesis.thesis')),
            ],
        ),
    ]
