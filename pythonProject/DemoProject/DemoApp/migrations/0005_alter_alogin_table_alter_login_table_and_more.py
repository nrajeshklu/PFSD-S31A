# Generated by Django 5.0 on 2024-01-09 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DemoApp', '0004_rename_ausername_alogin_auser'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='alogin',
            table='admin_table',
        ),
        migrations.AlterModelTable(
            name='login',
            table='login_table',
        ),
        migrations.AlterModelTable(
            name='user',
            table='user_table',
        ),
    ]
