# Generated by Django 4.1.13 on 2024-02-16 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0002_product_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.URLField(blank=True, null=True),
        ),
    ]
