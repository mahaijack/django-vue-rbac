# Generated by Django 3.0.5 on 2020-04-10 02:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_deleted',
        ),
    ]