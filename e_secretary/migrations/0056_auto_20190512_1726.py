# Generated by Django 2.2 on 2019-05-12 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_secretary', '0055_auto_20190506_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='cert_type',
            field=models.CharField(choices=[('ENERGOS', 'Ενεργού Φοιτητή'), ('ARMY', 'Στρατολογική Χρήσης'), ('GRADES', 'Αναλυτική Βαθμολογία')], max_length=10),
        ),
    ]
