# Generated by Django 4.0.2 on 2022-03-13 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_servicehelp'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='header',
            field=models.TextField(default=True, verbose_name='Загаловок'),
        ),
        migrations.AddField(
            model_name='contact',
            name='image',
            field=models.ImageField(default=True, upload_to='', verbose_name='Фото'),
        ),
    ]
