# Generated by Django 4.0.2 on 2022-03-28 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0035_catalog_alter_product_options_product_created_at'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Catalog',
            new_name='CatalogHead',
        ),
    ]
