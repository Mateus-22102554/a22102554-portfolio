# Generated by Django 4.0.4 on 2022-05-21 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_pontuacaoquizz'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('ano', models.IntegerField()),
                ('semestre', models.IntegerField()),
                ('ects', models.IntegerField()),
            ],
        ),
    ]