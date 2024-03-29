# Generated by Django 4.0.2 on 2022-03-24 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0034_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Названиe')),
                ('text', models.TextField(max_length=255, verbose_name='Описание')),
            ],
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-created_at'], 'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
