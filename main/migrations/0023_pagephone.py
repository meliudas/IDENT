# Generated by Django 4.0.2 on 2022-03-14 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_newsdetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pagephone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
        ),
    ]
