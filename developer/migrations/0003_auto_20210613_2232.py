# Generated by Django 3.1.8 on 2021-06-13 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('developer', '0002_auto_20210612_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dakauser',
            name='password',
            field=models.CharField(max_length=30),
        ),
    ]
