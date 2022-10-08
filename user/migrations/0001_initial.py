# Generated by Django 4.1.2 on 2022-10-06 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=15)),
                ('message', models.TextField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=250, null=True)),
                ('is_telegram', models.BooleanField(default=False)),
                ('is_web', models.BooleanField(default=False)),
                ('is_done', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
