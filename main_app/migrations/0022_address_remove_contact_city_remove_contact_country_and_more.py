# Generated by Django 4.0 on 2022-01-23 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0021_locationmap'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=300)),
                ('state', models.CharField(max_length=300)),
                ('country', models.CharField(max_length=300)),
            ],
        ),
        migrations.RemoveField(
            model_name='contact',
            name='city',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='country',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='state',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='street',
        ),
    ]