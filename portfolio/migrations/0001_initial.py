# Generated by Django 4.0.4 on 2022-05-16 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=30)),
                ('data', models.DateField()),
                ('titulo', models.CharField(max_length=30)),
                ('descricao', models.TextField()),
            ],
        ),
    ]