# Generated by Django 3.1.4 on 2021-03-19 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0005_auto_20210319_0916'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name': 'Сообщение', 'verbose_name_plural': 'Сообщеня'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Профиль', 'verbose_name_plural': 'Профили'},
        ),
    ]
