# Generated by Django 4.1 on 2022-08-16 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppMVTalfonso', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='integrantes',
            name='edad',
            field=models.IntegerField(),
        ),
    ]