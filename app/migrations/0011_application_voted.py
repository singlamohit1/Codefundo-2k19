# Generated by Django 2.2.4 on 2019-08-17 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_application_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='voted',
            field=models.BooleanField(default=False),
        ),
    ]
