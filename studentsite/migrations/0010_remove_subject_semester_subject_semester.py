# Generated by Django 4.0.2 on 2022-03-22 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studentsite', '0009_remove_subject_semester_subject_semester_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='semester',
        ),
        migrations.AddField(
            model_name='subject',
            name='semester',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='studentsite.semester'),
        ),
    ]
