# Generated by Django 4.0.2 on 2022-03-17 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_new_is_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='new',
            options={'ordering': ['-date'], 'verbose_name': 'New', 'verbose_name_plural': 'News'},
        ),
        migrations.RemoveField(
            model_name='new',
            name='created_at',
        ),
        migrations.AddField(
            model_name='new',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='new',
            name='image',
            field=models.ImageField(upload_to='news', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='new',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Актуально'),
        ),
        migrations.AlterField(
            model_name='new',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Заголовок'),
        ),
    ]
