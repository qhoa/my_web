# Generated by Django 4.2.1 on 2023-06-24 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='SubCategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.subcategory'),
        ),
    ]
