# Generated by Django 3.1.7 on 2021-04-24 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('value', models.JSONField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=10)),
                ('path', models.TextField()),
                ('params', models.TextField()),
                ('data', models.JSONField(default=dict)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('show', models.BooleanField()),
                ('page', models.TextField()),
                ('theme', models.TextField()),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
