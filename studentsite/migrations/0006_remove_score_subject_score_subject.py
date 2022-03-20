# Generated by Django 4.0.2 on 2022-03-20 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studentsite', '0005_subject_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='subject',
        ),
        migrations.AddField(
            model_name='score',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='studentsite.subject'),
        ),
    ]
