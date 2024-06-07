# Generated by Django 5.0.6 on 2024-06-07 06:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
        ('thesis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('s3_url', models.URLField()),
                ('expires', models.DateTimeField()),
                ('uploader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.student')),
            ],
        ),
    ]
