# Generated by Django 4.2.3 on 2023-08-08 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dsa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dsa',
            name='dvote',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='dsa',
            name='evote',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='dsa',
            name='ivote',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='dsa',
            name='mvote',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Vote',
        ),
    ]
