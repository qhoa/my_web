# Generated by Django 4.2.1 on 2023-06-24 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_category_subcategory_products'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MainCategory',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='name',
        ),
        migrations.AddField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Products',
        ),
    ]