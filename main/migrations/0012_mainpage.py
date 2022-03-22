# Generated by Django 4.0.3 on 2022-03-11 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_delete_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('titles', models.CharField(max_length=255, verbose_name='Название')),
                ('descriptions', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='', verbose_name='Фото')),
            ],
        ),
    ]