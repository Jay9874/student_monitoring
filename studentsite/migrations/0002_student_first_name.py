# Generated by Django 4.0.2 on 2022-03-20 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='first_name',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
