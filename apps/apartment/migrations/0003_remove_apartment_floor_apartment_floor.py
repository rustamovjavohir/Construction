# Generated by Django 4.0.4 on 2022-10-06 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartment', '0002_floor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartment',
            name='floor',
        ),
        migrations.AddField(
            model_name='apartment',
            name='floor',
            field=models.ManyToManyField(to='apartment.floor'),
        ),
    ]
