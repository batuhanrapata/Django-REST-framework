# Generated by Django 4.1.7 on 2023-03-23 14:00

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authApi', '0013_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=150), size=10),
        ),
    ]