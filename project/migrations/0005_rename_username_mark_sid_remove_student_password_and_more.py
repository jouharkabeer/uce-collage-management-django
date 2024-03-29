# Generated by Django 5.0.3 on 2024-03-17 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_rename_sid_mark_username_remove_student_sid_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mark',
            old_name='username',
            new_name='sid',
        ),
        migrations.RemoveField(
            model_name='student',
            name='password',
        ),
        migrations.RemoveField(
            model_name='student',
            name='username',
        ),
        migrations.AddField(
            model_name='mark',
            name='attendence',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='sid',
            field=models.AutoField(default='default_id', primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
