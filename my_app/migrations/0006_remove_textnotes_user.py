# Generated by Django 3.1.1 on 2020-12-16 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0005_textnotes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='textnotes',
            name='user',
        ),
    ]
