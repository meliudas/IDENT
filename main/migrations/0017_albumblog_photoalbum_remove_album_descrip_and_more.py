# Generated by Django 4.0.2 on 2022-03-12 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_album_descrip_album_imaged_album_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='', verbose_name='Фото')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoAlbum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='', verbose_name='Фото')),
            ],
        ),
        migrations.RemoveField(
            model_name='album',
            name='descrip',
        ),
        migrations.RemoveField(
            model_name='album',
            name='imaged',
        ),
        migrations.RemoveField(
            model_name='album',
            name='is_active',
        ),
    ]