# Generated by Django 4.0 on 2022-01-23 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0020_delete_map_delete_socailmedia'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocationMAp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('googleMap', models.URLField(max_length=10000)),
            ],
        ),
    ]
