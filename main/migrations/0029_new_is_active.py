# Generated by Django 4.0.2 on 2022-03-17 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_alter_new_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]