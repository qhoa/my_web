# Generated by Django 4.2.1 on 2023-06-23 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_rename_name_post_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Type',
            new_name='Category',
        ),
    ]