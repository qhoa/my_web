# Generated by Django 4.2.1 on 2023-06-24 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='gender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.genre'),
        ),
    ]