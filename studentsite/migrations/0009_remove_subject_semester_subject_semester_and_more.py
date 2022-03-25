# Generated by Django 4.0.2 on 2022-03-22 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentsite', '0008_remove_semester_student_semester_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='semester',
        ),
        migrations.AddField(
            model_name='subject',
            name='semester',
            field=models.ManyToManyField(to='studentsite.Semester'),
        ),
        migrations.RemoveField(
            model_name='subject',
            name='student',
        ),
        migrations.AddField(
            model_name='subject',
            name='student',
            field=models.ManyToManyField(to='studentsite.Student'),
        ),
    ]
