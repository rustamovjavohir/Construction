# Generated by Django 4.0.4 on 2022-10-10 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sendEmail', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='phone',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]