# Generated by Django 2.1.7 on 2019-04-03 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_secretary', '0031_simmetoxidrastiriotita_delivered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simmetoxidrastiriotita',
            name='delivered',
            field=models.BooleanField(default=False),
        ),
    ]
