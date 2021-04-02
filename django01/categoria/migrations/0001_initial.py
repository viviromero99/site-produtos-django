# Generated by Django 3.1.7 on 2021-03-30 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(db_index=True, max_length=70, unique=True)),
                ('slug', models.SlugField(max_length=70)),
            ],
            options={
                'db_table': 'categoria',
                'ordering': ('nome',),
            },
        ),
    ]
