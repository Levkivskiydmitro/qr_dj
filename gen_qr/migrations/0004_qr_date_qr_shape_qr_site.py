# Generated by Django 4.2.17 on 2025-02-06 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gen_qr', '0003_alter_qr_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='qr',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='qr',
            name='shape',
            field=models.CharField(default='квадратний', max_length=20),
        ),
        migrations.AddField(
            model_name='qr',
            name='site',
            field=models.CharField(default='Youtube', max_length=20),
        ),
    ]
