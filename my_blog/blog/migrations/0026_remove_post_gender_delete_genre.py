# Generated by Django 4.2.1 on 2023-06-25 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_post_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='gender',
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
    ]
