# Generated by Django 3.1.4 on 2021-02-12 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_auto_20210212_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='external_id',
            field=models.PositiveIntegerField(unique=True, verbose_name='ID пользователя в соц сети'),
        ),
    ]