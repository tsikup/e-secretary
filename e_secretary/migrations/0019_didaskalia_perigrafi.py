# Generated by Django 2.1.7 on 2019-04-02 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_secretary', '0018_remove_announcement_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='didaskalia',
            name='perigrafi',
            field=models.TextField(blank=True, null=True),
        ),
    ]