# Generated by Django 5.0.3 on 2024-03-18 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_rename_attendence_mark_attendance_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='types',
            new_name='type',
        ),
    ]
