# Generated by Django 4.0.2 on 2022-03-23 02:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentsite', '0011_remove_subject_semester_subject_semester'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='semester',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='student',
        ),
        migrations.RemoveField(
            model_name='achievement',
            name='semester',
        ),
        migrations.RemoveField(
            model_name='cocurriculum',
            name='semester',
        ),
        migrations.RemoveField(
            model_name='remark',
            name='semester',
        ),
        migrations.RemoveField(
            model_name='score',
            name='semester',
        ),
        migrations.RemoveField(
            model_name='score',
            name='subject',
        ),
        migrations.DeleteModel(
            name='Semester',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
    ]
