# Generated by Django 3.1.7 on 2021-03-31 00:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0002_auto_20210330_2015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='data_cadastro',
        ),
    ]
