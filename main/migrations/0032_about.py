# Generated by Django 4.0.2 on 2022-03-17 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_contphone'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('image', models.ImageField(upload_to='', verbose_name='Фото')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
        ),
    ]
