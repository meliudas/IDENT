# Generated by Django 4.0.2 on 2022-03-13 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_photoalbum_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='is_active',
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='service',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
    ]