# Generated by Django 3.2.4 on 2021-06-16 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0003_auto_20210616_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegroups',
            name='Yourname',
            field=models.CharField(default=-1.0, max_length=30),
            preserve_default=False,
        ),
    ]
