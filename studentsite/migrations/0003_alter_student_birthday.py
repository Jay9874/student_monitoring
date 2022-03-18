# Generated by Django 4.0.2 on 2022-03-18 00:20

from django.db import migrations, models
import pytz


class Migration(migrations.Migration):

    dependencies = [
        ('studentsite', '0002_student_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='birthday',
            field=models.DateField(default=pytz.timezone, null=True),
        ),
    ]
