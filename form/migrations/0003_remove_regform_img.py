# Generated by Django 3.2.8 on 2021-10-07 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_alter_regform_mobile_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='regform',
            name='img',
        ),
    ]