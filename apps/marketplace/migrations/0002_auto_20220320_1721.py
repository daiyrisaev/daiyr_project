# Generated by Django 3.2 on 2022-03-20 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emailuser',
            options={'verbose_name': 'пользаватель', 'verbose_name_plural': 'пользаватели'},
        ),
        migrations.RemoveField(
            model_name='emailuser',
            name='category',
        ),
    ]
