# Generated by Django 4.0 on 2021-12-27 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_hero'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hero',
            name='hero_title',
        ),
        migrations.AlterField(
            model_name='hero',
            name='hero_pic',
            field=models.ImageField(upload_to='media/pics'),
        ),
    ]