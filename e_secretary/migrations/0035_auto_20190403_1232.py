# Generated by Django 2.1.7 on 2019-04-03 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_secretary', '0034_auto_20190403_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.CharField(choices=[('HMTY', 'HMTY'), ('CEID', 'CEID')], max_length=20),
        ),
    ]
