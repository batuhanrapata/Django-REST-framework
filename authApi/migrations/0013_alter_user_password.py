# Generated by Django 4.1.7 on 2023-03-23 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authApi', '0012_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=150),
        ),
    ]
