# Generated by Django 2.2.1 on 2019-06-06 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='connection',
            name='active_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
