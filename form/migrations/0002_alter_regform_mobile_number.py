# Generated by Django 3.2.8 on 2021-10-07 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regform',
            name='Mobile_Number',
            field=models.PositiveBigIntegerField(),
        ),
    ]