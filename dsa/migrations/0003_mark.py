# Generated by Django 4.2.3 on 2023-08-08 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dsa', '0002_dsa_dvote_dsa_evote_dsa_ivote_dsa_mvote_delete_vote'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('pid', models.IntegerField(default=0)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
