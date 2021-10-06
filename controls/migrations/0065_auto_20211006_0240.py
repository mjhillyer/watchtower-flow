# Generated by Django 3.2.5 on 2021-10-06 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteapp', '0052_merge_0049_auto_20210423_1555_0051_auto_20210822_0328'),
        ('controls', '0064_auto_20211002_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='system',
            name='tags',
            field=models.ManyToManyField(related_name='system', to='siteapp.Tag'),
        ),
        migrations.AlterField(
            model_name='system',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]
