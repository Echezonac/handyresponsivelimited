# Generated by Django 4.0 on 2022-01-06 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_alter_testimony_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimony',
            name='message',
            field=models.TextField(max_length=100),
        ),
    ]
