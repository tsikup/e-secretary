# Generated by Django 2.1.7 on 2019-03-29 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_secretary', '0006_auto_20190329_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/announcements'),
        ),
        migrations.AlterField(
            model_name='secr_announcement',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/secr_announcements'),
        ),
    ]
