# Generated by Django 2.2.4 on 2019-08-16 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20190816_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='address',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='dob',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='fathers_name',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='mobile',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='pincode',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
