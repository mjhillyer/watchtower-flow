# Generated by Django 3.2.12 on 2022-03-30 16:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteapp', '0054_user_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='party',
            name='mobile_phone',
            field=models.CharField(blank=True, max_length=16, null=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')]),
        ),
        migrations.AddField(
            model_name='party',
            name='phone_number',
            field=models.CharField(blank=True, max_length=16, null=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')]),
        ),
    ]
