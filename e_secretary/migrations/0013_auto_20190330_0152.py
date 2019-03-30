# Generated by Django 2.1.7 on 2019-03-29 23:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('e_secretary', '0012_profile_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thesis',
            name='student_am',
        ),
        migrations.AddField(
            model_name='student',
            name='thesis',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='e_secretary.Thesis'),
        ),
    ]
