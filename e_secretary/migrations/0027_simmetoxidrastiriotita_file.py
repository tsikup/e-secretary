# Generated by Django 2.1.7 on 2019-04-02 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_secretary', '0026_auto_20190402_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='simmetoxidrastiriotita',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files'),
        ),
    ]