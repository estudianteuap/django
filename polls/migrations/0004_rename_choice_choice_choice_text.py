# Generated by Django 3.2.5 on 2021-07-13 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_rename_choice_text_choice_choice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='choice',
            new_name='choice_text',
        ),
    ]