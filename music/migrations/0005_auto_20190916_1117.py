# Generated by Django 2.2.5 on 2019-09-16 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_auto_20190916_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payementmethod',
            name='ecocash',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='payementmethod',
            name='lumicash',
            field=models.TextField(max_length=100),
        ),
    ]