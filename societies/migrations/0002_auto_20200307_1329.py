# Generated by Django 2.2 on 2020-03-07 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('societies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='votes',
            field=models.IntegerField(),
        ),
    ]
