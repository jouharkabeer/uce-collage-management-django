# Generated by Django 5.0.3 on 2024-03-18 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_alter_mark_sid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mark',
            old_name='sid',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='sid',
        ),
        migrations.AddField(
            model_name='student',
            name='id',
            field=models.BigAutoField(auto_created=True, default='default_id', primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
