# Generated by Django 4.2.17 on 2025-01-16 18:30

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
                ('username', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
