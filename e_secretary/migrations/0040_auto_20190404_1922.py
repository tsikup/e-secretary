# Generated by Django 2.1.7 on 2019-04-04 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('e_secretary', '0039_auto_20190404_1825'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orologio',
            old_name='didaskalia_id',
            new_name='didaskalia',
        ),
    ]